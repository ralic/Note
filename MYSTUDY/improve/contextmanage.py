# coding=utf-8
import contextlib
import urllib
# 上下文管理器(context manager)是Python2.5开始支持的一种语法，用于规定某个对象的使用范围。
# 一旦进入或者离开该使用范围，会有特殊操作被调用 (比如为对象分配或者释放内存)。它的语法形式是with...as...


# 类似于再先执行__enter__的代码，然后再try块中执行主要功能，finally中调用__exit__的代码
class MyContextManager(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        print "enter my context manager"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text = "close context manager"

    def test(self):
        print self.text

"""
    Typical usage:

        @contextmanager
        def some_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>

    This makes this:

        with some_generator(<arguments>) as <variable>:
            <body>

    equivalent to this:

        <setup>
        try:
            <variable> = <value>
            <body>
        finally:
            <cleanup>

"""


# 使用装饰器语法
@contextlib.contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

if __name__ == '__main__':
    with closing(urllib.urlopen("http://www.python.org")) as page:
        for line in page:
            print line