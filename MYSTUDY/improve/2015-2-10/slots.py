# coding=utf-8
# 槽,拥有__slots__属性的类，实例化对象时，不会给实例自动分配__dict__
# 对于拥有 __slots__ 属性的类的实例 Obj 来说，只能对 Obj 设置 __slots__ 中有的属性.


class Frozen(object):
    __slots__ = ["ice", "cream"]

    # 设定了slots之后，实例的初始化属性若不包含在slots内，将会产生错误
    # def __init__(self, a):
    #     self.a = a

    def other(self):
        pass

def testfrozen():
    f = Frozen()
    f.ice = "ice"
    f.other()
    print Frozen.__dict__
    # print f.__dict__
    print f.__slots__
    # 通过slots简介设置属性
    f.__slots__[0] = 100
    print f.ice

if __name__ == '__main__':
    testfrozen()
