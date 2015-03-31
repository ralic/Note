# coding=utf-8
import functools
# like -> function = function_wrapper(function)


# use class as decorator
class class_wapper(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __call__(self, *args, **kwargs):
        return self.wrapped(*args, **kwargs)


@class_wapper
def function(today=1):
    return today


def function_wrapper(wrapped):
    def _wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs)
    return _wrapper


def function_wrapper_attr(wrapped):
    def _wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs)
    # 显式将被包装的函数的部分属性复制给嵌套函数
    _wrapper.__name__ = wrapped.__name__
    _wrapper.__doc__ = wrapped.__name__
    return _wrapper


@function_wrapper
def function2():
    pass

print function2.__name__, function2.__dict__
@function_wrapper_attr
def function2():
    pass

print function2.__name__, function2.__dict__

def function_wrapper(wrapped):
    # 利用functools的wraps方法隐式复制__name__、__doc__、__module__
    @functools.wraps(wrapped)
    def _wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs)
    return _wrapper


@function_wrapper
def func():
    pass


import functools
class function_wrapper(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped
        functools.update_wrapper(self, wrapped)
    def __call__(self, *args, **kwargs):
        return self.wrapped(*args, **kwargs)

class Class(object):
    @function_wrapper
    def method(self):
        pass

    @classmethod
    def cmethod(cls):
        pass

    @staticmethod
    def smethod():
        pass
