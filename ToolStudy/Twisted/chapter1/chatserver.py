from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor


class ChatProtocol(LineReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.name = None
        self.state = "Register"

    def connectionMade(self):
        self.sendLine("What's your name")

    def connectionLost(self, reason=None):
        if self.name in self.factory.users:
            del self.factory.users[self.name]
            self.broadcastMessage("%s has left the channel." % self.name)

    def broadcastMessage(self, message):
        for name, protocol in self.factory.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)

    def lineReceived(self, line):
        if self.state == "Register":
            self.handle_register(line)
        else:
            self.handle_chat(line)

    def handle_register(self, name):
        if name in self.factory.users:
            self.sendLine("Name taken, please choose another.")
            return
        self.sendLine("Welcome, %s!" % (name,))
        self.broadcastMessage("%s has joined the channel." % (name,))
        self.name = name
        self.factory.users[name] = self
        self.state = "CHAT"

    def handle_chat(self, message):
        message = "<%s> %s" % (self.name, message)
        self.broadcastMessage(message)


class ChatFactory(Factory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        return ChatProtocol(self)

reactor.listenTCP(8000, ChatFactory())
reactor.run()