# coding=utf-8
"""
属性拦截：
    person.name # Fetch attribute value
    person.name = value # Change attribute value
========================================================
• The __getattr__ and __setattr__ methods, for routing undefined attribute fetches
and all attribute assignments to generic handler methods.
路由到未定义属性和获取任意属性分配的通用处理方法

• The __getattribute__ method, for routing all attribute fetches to a generic handler
method.
路由到任意属性的通用处理方法

• The property built-in, for routing specific attribute access to get and set handler
functions.
路由到特定的属性（get）， 特定的属性获取（set）

• The descriptor protocol, for routing specific attribute accesses to instances of classes
with arbitrary get and set handler methods, and the basis for other tools such as
properties and slots.
描述器协议，路由特定属性入口（比如一个类实例带有任意的get或set方法。。。）

Properties:
    property protocol 允许我们为函数或方法提供特定的属性操作（get、set或delete）。即可以把一个方法当作属性一样调用。
    这种特性可以由的property类来构建:
        attribute = property(fget, fset, fdel, doc)             # 所有参数的默认值都为None（None表示不支持该操作，默认所有协议的操作都不支持）。

    fget is a function to be used for getting an attribute value, and likewise
    fset is a function for setting,
    fdel Is a function for del'ing, a attribute.

    Typical use is to define a managed attribute x:
        class C(object):
        def getx(self): return self._x
        def setx(self, value): self._x = value
        def delx(self): del self._x
        x = property(getx, setx, delx, "I'm the 'x' property.")

    Decorators make defining new properties or modifying existing ones easy:

    class C(object):
        @property
        def x(self):
            "I am the 'x' property."
            return self._x
        @x.setter
        def x(self, value):
            self._x = value
        @x.deleter
        def x(self):
            del self._x
"""


# property protocol
# 1.first Example
class Person(object):
    def __init__(self, name):
        self._name = name

    def getname(self):
        print "fetch..."
        return self._name

    def setname(self, value):
        print "change..."
        self._name = value

    def delname(self):
        print "remove.."
        del self._name

    name = property(getname, setname, delname, "name property docs")

    @staticmethod
    def test_person():
        bob = Person("Bob Smith")
        print bob.name               # Runs getname
        bob.name = 'Robot Smith'     # Runs setname
        print bob.name
        del bob.name                # Runs delname

        print "-"*20
        sue = Person("sue")
        print sue.name
        print Person.name.__doc__


# 2.properties inherited
class Son(Person):
    """继承父类的properties"""

    @staticmethod
    def sontest():
        s = Son("loser boy go die go live go everywhere")
        print s.name


# 3.computed attributes
class PropSquare(object):
    def __init__(self, start):
        self.value = start

    def getx(self):
        return self.value ** 2

    def setx(self, value):
        self.value = value

    x = property(getx, setx)

    @staticmethod
    def test():
        p = PropSquare(3)
        q = PropSquare(32)
        print p.x
        p.x = 4
        print p.x
        print q.x


# 4.coding properties with decorators
#   class Person:
#       @property
#       def name(self): ... # Rebinds: name = property(name)#, 默认做第一个参数
class NewPerson(object):
    def __init__(self, name):
        self._name = name

    @property                       # name = property(name)
    def name(self):
        return self._name

    @name.setter                    # name = name.setter(name)
    def name(self, value):
        self._name = value

    @name.deleter                   # name = name.deleter(name)
    def name(self):
        del self._name


