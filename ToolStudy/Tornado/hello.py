# coding=utf-8
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.options import define, options, parse_command_line
#
# 从命令行中读取port参数的值，默认为8080
# （命令名称，默认值，帮助信息，值的类型）
# 举例：python hello.py --port=8080 --jinkela=hahaha
define("port", default=8000, help="run on the given port", type=int)
define("jinkela", default="mamade", help="I need jinkala", type=str)


# 请求处理函数类，继承自tornado.web.RequestHandler
# 处理请求是，该类被实例化，然后调用对应的HTTP请求方法（如get、post、put等）
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        greeting = self.get_argument("greeting", "Hello")  # 获得url的query字符串中greeting的值，若不存则为Hello
        self.write(greeting + ', friendly user!')   # 输出响应内容


if __name__ == '__main__':
    parse_command_line()    # 解析命令
    # 创建Application实例，通过handlers参数来指定由哪个类响应请求
    app = Application(handlers=[(r"/", IndexHandler)])
    # 将app传递给HTTPServer对象， 然后监听指定的端口
    httpserver = HTTPServer(app)
    httpserver.listen(options.port)
    # print options.port
    # print options.jinkela
    # 一切准备工作就绪后，创建一个IOLoop实例
    IOLoop.instance().start()