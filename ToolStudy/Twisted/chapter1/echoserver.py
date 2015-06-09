# coding=utf-8
from twisted.internet import protocol, reactor


# transport表示网络在两个终端的连接（TCP、UDP等）
class Echo(protocol.Protocol):
    # 将从客户端接收到的数据data稍作修饰，然后通过transport返回给客户端
    def dataReceived(self, data):
        # 将数据写入到物理连接
        self.transport.write("you said:" + data)

    def connectionMade(self):
        print "%s is connected" % self.transport.getPeer()




class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


# 监听端口
reactor.listenTCP(8000, EchoFactory())
reactor.run()
