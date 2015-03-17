# coding=utf-8
# 命名空间字典, 属性点号运算实际上在内部就是字典的索引运算
# 属性点号运算和字典索引的区别在于，属性点号运算会搜索继承树，即子类没找到属性，会链接到父类中继续查找。而字典索引不会搜索。
# 比如object.attribute  《=》  object.__dict__["attribute"]
# 继承的情况下，__dict__

class Test(object):
    def __init__(self, x):
        self.x = x

    def getx(self):
        return self.x

class SonTest(Test):
    def __init__(self, x, y):
        Test.__init__(self, x)
        self.y = y

if __name__ == '__main__':
    # 类级字典
    print Test.__dict__
    # 对象级字典，只是包含__init__定义的属性
    print Test(100).__dict__
    # 字典索引运算
    Test.__dict__["__init__"](Test(100), 100)
    t = Test(100)
    print t.__dict__["x"]

    # 继承的情况
    print SonTest.__dict__