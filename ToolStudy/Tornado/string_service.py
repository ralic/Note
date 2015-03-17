# coding=utf-8
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.options import options, define, parse_command_line
import textwrap


define("port", default=8000, help="...", type=int)


class ReverseHandler(RequestHandler):
    # 这个input参数将包含匹配处理函数正则表达式第一个括号里的字符串
    def get(self, input, input2):
        self.write(input[::-1]+"\n")
        self.write(input2)


# post请求，在命令行中curl <url> -d 参数
# curl -d/--data <data>   HTTP POST方式传送数据
class WrapHandler(RequestHandler):
    def post(self, *args, **kwargs):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))

if __name__ == '__main__':
    parse_command_line()
    app = Application(handlers=[(r"/reverse/(\w+)(\d+)", ReverseHandler), (r'/wrap', WrapHandler)])
    httpserver = HTTPServer(app)
    httpserver.listen(options.port)
    IOLoop.instance().start()