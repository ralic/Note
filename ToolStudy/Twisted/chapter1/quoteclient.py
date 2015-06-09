# coding=utf-8
from twisted.internet import reactor, protocol
# @UndefinedVariable
# 通过factory来保持协议的状态

class QuoteProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.sendQuote()

    def sendQuote(self):
        self.transport.write(self.factory.quote)

    def dataReceived(self, data):
        print "Recive quote:", data
        self.transport.loseConnection()

class QuoteClientFactory(protocol.ClientFactory):
    def __init__(self, quote):
        self.quote = quote

    def buildProtocol(self, addr):
        return QuoteProtocol(self)

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed:", reason.getErrorMessage()
        maybeStopReactor()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost", reason.getErrorMessage()
        maybeStopReactor()

def maybeStopReactor():
    global quote_counter
    quote_counter -= 1
    if not quote_counter:
        reactor.stop()

quotes = [
    "You snooze you lose %d" % d for d in range(1000)
 ]

quote_counter = len(quotes)
for q in quotes:
    reactor.connectTCP("localhost", 8000, QuoteClientFactory(q))
reactor.run()