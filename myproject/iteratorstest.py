# -*- coding: utf8 -*-
#
# python 迭代器(注：生成器只是一种特殊的迭代器)
#


class Fib:
    """生成斐波那契数列的迭代器
    """
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        """
        当调用iter（）时，会自动调用该方法；在for循环中会自动调用该方法。
        该方法必须返回实现了next方法的对象
        """
        self.a = 0
        self.b = 1
        return TestNext(10)

    def next(self):
        """
        获取下一个迭代的值，一但不符合条件，就出发StopIteration来结束迭代
        """
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


class TestNext:
    def __init__(self, min):
        self.min = min
        self.a = 0
    def next(self):
        if self.a >= self.min:
            raise StopIteration
        self.a += 1
        return self.a


def caculate(x, b):
    def next():
        print x, b
    return next

#
# class LazyRules:
#     rules_filename = 'plural6-rules.txt'
#
#     def __init__(self):
#         self.pattern_file = open(self.rules_filename, encoding='utf-8')
#         self.cache = []
#
#     def __iter__(self):
#         self.cache_index = 0
#         return self
#
#     def __next__(self):
#         self.cache_index += 1
#         if len(self.cache) >= self.cache_index:
#             return self.cache[self.cache_index - 1]
#
#         if self.pattern_file.closed:
#             raise StopIteration
#
#         line = self.pattern_file.readline()
#         if not line:
#             self.pattern_file.close()
#             raise StopIteration
#
#         pattern, search, replace = line.split(None, 3)
#         funcs = build_match_and_apply_functions(
#             pattern, search, replace)
#         self.cache.append(funcs)
#         return funcs
#
# rules = LazyRules()
if __name__ == "__main__":
    fib = Fib(100)
    print list(fib)
    sorted()

