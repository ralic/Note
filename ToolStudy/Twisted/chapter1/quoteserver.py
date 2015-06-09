# coding=utf-8
# @UndefinedVariable
from twisted.internet import reactor, protocol
from twisted.internet.protocol import Factory, connectionDone


class QuoteProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numConnections += 1

    def dataReceived(self, data):
        print "Number of active connections: %d" % self.factory.numConnections
        print ">Recived:''%s''\n>   Sending:''%s''" % (data, self.getQuote())
        self.transport.write(self.getQuote())
        self.updateQuote(data)

    def connectionLost(self, reason=connectionDone):
        self.factory.numConnections -= 1

    def getQuote(self):
        return self.factory.quote

    def updateQuote(self, data):
        self.factory.quote = data


# 保持所有事件的状态
class QuoteFactory(Factory):
    numConnections = 0
    protocol = QuoteProtocol

    def __init__(self, quote=None):
        self.quote = quote or "I think the weather is well!"

    def buildProtocol(self, addr):
        return self.protocol(self)


reactor.listenTCP(8000, QuoteFactory())
reactor.run()


