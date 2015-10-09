# coding=utf-8
"""
descriptor是一种拦截属性访问的技术。
    1.实际上property就是一种特殊的descroptr, 它实现的是利用属性访问的方式来执行method（方法）。
    2.descriptor 还包括slots...
    3.Functionally speaking, the descriptor protocol allows us to route a specific attribute’s
get, set, and delete operations to methods of a separate class’s instance object that we
provide. This allows us to insert code to be run automatically on attribute fetches and
assignments, intercept attribute deletions, and provide documentation for the attributes if desired.

descr.__get__(self, obj, type=None) --> value

descr.__set__(self, obj, value) --> None

descr.__delete__(self, obj) --> None

这是所有描述器方法。一个对象具有其中任一个方法就会成为描述器，从而在被当作对象属性时重写默认的查找行为。

如果一个对象同时定义了 __get__() 和 __set__(),它叫做资料描述器(data descriptor)。
仅定义了 __get__() 的描述器叫非资料描述器(常用于方法，当然其他用途也是可以的)

资料描述器和非资料描述器的区别在于：相对于实例的字典的优先级。
如果实例字典中有与描述器同名的属性，如果描述器是资料描述器，优先使用资料描述器，如果是非资料描述器，
优先使用字典中的属性。(译者注：这就是为何实例 a 的方法和属性重名时，比如都叫 foo Python会在访问
a.foo 的时候优先访问实例字典中的属性，因为实例函数的实现是个非资料描述器)

要想制作一个只读的资料描述器，需要同时定义 __set__ 和 __get__,并在 __set__ 中引发一个 AttributeError 异常。
定义一个引发异常的 __set__ 方法就足够让一个描述器成为资料描述器。

"""


# 1.Descriptor method arguments
class Descriptor(object):
    def __get__(self, instance, owner):
        print self, instance, owner,


class Subject(object):               # Add "(object)" in 2.X
    attr = Descriptor()                 # Descriptor instance is class att

    @staticmethod
    def test():
        x = Subject()
        print x.attr                  # x.attr -> Descriptor.__get__(Subject.attr, x, Subject)
        print Subject.attr

Subject.test()