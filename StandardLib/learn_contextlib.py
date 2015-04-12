# coding=utf-8
# 用于处理上下文管理器和with语句
# 上下文管理器负责一个代码块中的资源。主要是在代码块执行前准备，代码块执行后收拾。
# 可能在进入代码块时，创建资源，退出代码块时清理资源。如文件的打开和关闭。


# 1.传统方法，构造一个包含enter和exit方法的类实现上下文管理器
class MyContext(object):
    """
    通过with启用，__enter__用于返回对象，__exit__用于清理资源。
    先执行__enter__的代码,然后执行with块内的代码，最后执行__exit__块的代码
    """
    def __init__(self):
        print "__init__"

    def __enter__(self):
        """返回一个对象"""
        print "__enter__"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """exc_type 异常类型
           exc_val 异常信息
           exc_tb traceback 对象
        """
        print "__exit__"
        print "type", exc_type
        print "val", exc_val
        print "tb", exc_tb


def test_mycontext():
    with MyContext() as m:
        print m.__class__
        print "Work in the context"
        raise RuntimeError("error hello")
    print "Work over!!!"


# 2 利用contextlib模块的contextmanager实现
import contextlib


@contextlib.contextmanager
def make_context():
    """
            @contextmanager
        def some_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>
    """
    print "enter"
    try:
        yield {}
    except RuntimeError, err:
        print "Error err"
    finally:
        print "exit"


if __name__ == '__main__':
    # test_mycontext()
    with make_context() as m:
        m.setdefault("hello", [])
        print m

