# coding=utf-8
import numpy


# 向量相加
# arange
def numpysum(n):
    a = numpy.arange(n) ** 2
    print a
    b = numpy.arange(n) ** 3
    print b
    c = a + b
    print c
    return c

numpysum(10)
