# coding=utf-8
# 描述器
# 一般来说，一个描述器是一个有“绑定行为”的对象属性(object attribute)，
# 它的访问控制被描述器协议方法重写。这些方法是 __get__(), __set__(), 和 __delete__() 。
# 有这些方法的对象叫做描述器。
# 默认对属性的访问控制是从对象的字典里面(__dict__)中获取(get), 设置(set)和删除(delete)它。
# 举例来说， a.x 的查找顺序是, a.__dict__['x'] , 然后 type(a).__dict__['x'] ,
# 然后找 type(a) 的父类(不包括元类(metaclass)).如果查找到的值是一个描述器,
# Python就会调用描述器的方法来重写默认的控制行为。这个重写发生在这个查找环节的哪里取决于定义了哪个描述器方法。
# 注意, 只有在新式类中时描述器才会起作用。(新式类是继承自 type 或者 object 的类)

"""
描述器协议：
descr.__get__(self, obj, type=None) --> value
descr.__set__(self, obj, value) --> None
descr.__delete__(self, obj) --> None
资料描述器：同时定义了__get__()和__set__()
非资料描述器：仅仅定义了__get__()

资料描述起先于实例变量，实例变量先于非资料描述器:
    描述器的调用是因为 __getattribute__()
    重写 __getattribute__() 方法会阻止正常的描述器调用
    __getattribute__() 只对新式类(继承自object的类)的实例可用
    object.__getattribute__() 和 type.__getattribute__() 对 __get__() 的调用不一样
    资料描述器总是比实例字典优先。
    非资料描述器可能被实例字典重写。(非资料描述器不如实例字典优先)
"""


class C(object):
    def getx(self):
        print "get x"
        return self.__x

    def setx(self, value):
        print "set x to", value
        self.__x = value


    def delx(self):
        print "del x"
        del self.__x

    x = property(getx, setx, delx, "I'm the 'x' property.")


# 定义一个资料描述器
class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating', self.name
        self.val = val


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()
print m.x

m.x = 20
print m.x
print m.y