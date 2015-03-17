# -*- coding: utf-8 -*-


def choose_class(name):
    if name == "foo":
        class Foo:
            pass
        return Foo
    else:
        class Bar:
            pass
        return Bar


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    使用函数做元类
    类名，父类，属性字典
    """
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        # 将所有不以双下划线开头的属性名变成大写
        print name, val
        if not name.startswith("__"):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val
    # 最后让type创建该元类
    return type(future_class_name, future_class_parents, uppercase_attr)

# 作用于模块中所有类， 所有类的创建，会默认调用
# __metaclass__ = upper_attr


class Foo():
    def __init__(self):
        self.bar = "bip"


    def good(self):
        print "good"


# 注意type和int ，str一样，所以你可以继承它

class UpperAttrMetaclass(type):
    # __new__ 在 __init__之前被调用, 第一个参数类似于self.指明是创建的是哪个类对象，默认使用mcs为第一个参数的名字
    # 这个方法负责创建并且返回对象(初始化类)
    #  __init__ 方法只是初始化对象参数
    # 平时很少用 __new__, 除非你想要控制对象的创建
    def __new__(mcs, claname,
                bases, dct):
        print mcs, claname, bases, dct
        uppercase_attr = {}
        for name, val in dct.items():
            print name, val
            if not name.startswith("__"):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        # 使用super关键字来返回，调用直接父类的__new__方法
        return super(UpperAttrMetaclass, mcs).__new__(mcs, claname, bases, uppercase_attr)
        # 直接调用元类type的__new__方法
        # return type.__new__(mcs, claname, bases, uppercase_attr)


class Hello:
    # 类创建默认调用UpperAttrMetaclass的__new__方法来初始化类对象（在比如则加或删除属性等）。
    __metaclass__ = UpperAttrMetaclass
    a = 100
    def check(self):
        pass

Hello()
# test = UpperAttrMetaclass("Foo2", (), {"name": "hha"})
# print hasattr(test, "NAME")
