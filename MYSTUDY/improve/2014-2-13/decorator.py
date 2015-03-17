# coding=utf-8
# 装饰器again
# __call__ 实现了该函数的类，它的实例可以像函数一样直接调用,即是实例本身实现函数的功能。
# __call__的作用在于保存状态信息（即可以使用类中其他方法或属性）


# example 1， 简单调用__call__方法
class Callee:
    def __call__(self, *args, **kwargs):
        print "call me!~"
        print args
        print kwargs


def test1():
    t = Callee()
    t()
    t(1, 2, 3, name="call", bron="born")


# exapmle2， 与类的属性和方法交互
class CalleeTwo:
    def __init__(self, value):
        self.value = value

    def __call__(self, *args, **kwargs):
        self.printvalue()
        return self.value * 2

    def printvalue(self):
        print self.value


def test2():
    c = CalleeTwo(100)
    result = c()
    print result


# example 3 , 回调函数
class Myspider:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print "my name is:", self.name


def test3():
    sp1 = Myspider("s1")
    sp2 = Myspider("s2")
    def sp(command=None):
        if not command:
            return None
        else:
            return command()
    sp(command=sp1)
    sp(command=sp2)


# example 4, 通过类来实现装饰器
class function_wrapper(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __call__(self, *args, **kwargs):
        return self.wrapped(*args, **kwargs)


@function_wrapper    # ==> functions_wrapper(function)
def function():
    print "I am invoked...."


@function_wrapper
def function2(length):
    return range(length)


def test4():
    function()
    print function2(10)


# example 5， 通过函数实现装饰器
def function_wrappper(warpped):
    def _wrapper(*args, **kwargs):
        return warpped(*args, **kwargs)
    return _wrapper


def test5():
    @function_wrappper
    def functions():
        print "test5...."
    functions()


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()