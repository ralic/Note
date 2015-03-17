# coding=utf-8
# 描述符:定义于类层次上

# first：一个类可以委托另一个类来管理其特性
# __set__ 在任何特性被设置时调用
# __get__ 在任何特性被读取时调用
# __delete__ 在使用del删除特性是调用
# 以上三者都在__dict__之前被调用

class UpperString(object):
    def __init__(self):
        self._value = ''

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value

class MyClass(object):
    attribute = UpperString()


def main():
    instance = MyClass()
    print instance.attribute
    instance.attribute = "my value"
    print instance.attribute
    print instance.__dict__
    instance.new_attr = 1
    print instance.__dict__

if __name__ == '__main__':
    main()