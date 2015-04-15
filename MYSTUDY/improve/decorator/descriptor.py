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

class B(object):
    x = None

    @property
    def x(self):
        return 100


c = C()
c.x = 100
print c.x
del c.x

b = B()
print b.x