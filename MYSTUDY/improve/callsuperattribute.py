# coding=utf-8
# 访问超超类中的方法
# 静态方法(静态方法是给类操作的，传递实例作为参数，多用于记录实例的状态，而不是行为，比如统计实例的个数)
#   静态方法更适合处理一个类的数据
# 类方法（类方法,需要将类对象（不是实例对象）作为第一个参数传递,不需要显示提供类名，会自动传递类对象）
#   类方法适合处理多个层级（即存在继承关系）中每个类不同的数据
# 类方法和静态方法都可以被类和实例调用。而实例方法只能被实例调用。
"""
实例方法，静态方法，类方法
Transformation	Called from an Object	Called from a Class
    function	    f(obj, *args)	            f(*args)
    staticmethod	f(*args)	                f(*args)
    classmethod	    f(type(obj), *args)	        f(klass, *args)

class StaticMethod(object):
 "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

 def __init__(self, f):
      self.f = f

 def __get__(self, obj, objtype=None):
      return self.f

class ClassMethod(object):
     "Emulate PyClassMethod_Type() in Objects/funcobject.c"

     def __init__(self, f):
          self.f = f

     def __get__(self, obj, klass=None):
          if klass is None:
               klass = type(obj)
          def newfunc(*args):
               return self.f(klass, *args)
          return newfunc
"""
class Kls(object):
    numInstance = 0

    def __init__(self):
        Kls.numInstance += 1

    @staticmethod
    def printstatic():
        print "static method", Kls.numInstance

    @classmethod
    def printinstance(cls):
        print "instance num is ", cls.numInstance


class KlsSon(Kls):
    @classmethod
    def printinstance(cls):
        print "Extra stuff...", cls
        Kls.printinstance()


class Other(Kls):
    pass


def testkls():
    x, y = KlsSon(), Kls()
    x.printinstance()
    KlsSon.printinstance()

    y.printinstance()
    Kls.printinstance()

    z = Other()
    z.printinstance()

    x.printstatic()
    y.printstatic()
    z.printstatic()

if __name__ == '__main__':
    testkls()

