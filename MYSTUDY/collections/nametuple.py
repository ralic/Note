# coding=utf-8
# 命名元祖， 返回一个包含名字的tuple子类
from collections import namedtuple

"""
    typename指定类型名，field_names指定tuple中每个参数的名字（field_names可以是list、tuple,或者以逗号空格分隔的字符串）
    def namedtuple(typename, field_names, verbose=False, rename=False):
    Returns a new subclass of tuple with named fields.

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessable by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)
"""

# 构造一个名为Point的tuple子类，
Point = namedtuple("Point", ["x", "y"])
print Point

# 实例化一个Point
p = Point(x=1, y=2)
# 通过索引访问
print p[0] + p[1]
x, y = p
print x, y
# 通过属性访问
print p.x, p.y
# 转换为有序字典后，通过名称访问对应元素
d = p._asdict()
print d
print d['x'], d['y']

# 转换为tuple、list
print tuple(p), list(p)

