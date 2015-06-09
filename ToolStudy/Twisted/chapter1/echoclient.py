# coding=utf-8
from twisted.internet import reactor, protocol
# @UndefinedVariable


# Protocol描述如何执行网络中的异步事件(对应协议具体的实现)
class EchoClient(protocol.Protocol):
    # 当和另一个终端建立连接时被调用
    def connectionMade(self):
        self.transport.write("Hello")       # 连接建立完成时，发送一个hello给服务端
        print self.transport.getPeer()
        print self.transport.getHost()

    # 当接收到数据时被调用，接收服务端返回的数据
    def dataReceived(self, data):
        print "Server said:", data
        self.transport.loseConnection()


# 事件工厂，通过为每个连接来创建事件（协议Protocol），
# 然后将其传递给reactor以注册回调
class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed"
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost"
        reactor.stop()

reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()

