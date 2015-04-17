# coding=utf-8
# 计算标准差
import math

def mean(alist):
    return sum(alist) / float(len(alist))


def stddev(alist):
    n = len(alist)
    list_mean = mean(alist)
    sd = math.sqrt(sum([(num - list_mean) ** 2 for num in alist]) / float(n))
    return sd


# 变异系数= 标准差 /  均值
def cv(alist):
    sd = stddev(alist)
    means = mean(alist)
    return sd / means

if __name__ == '__main__':
    print mean([1, 2, 3])
    print mean([11, 12, 13])
    print mean([0.1, 0.1, 0.1])
    print stddev([6, 7, 5, 10])
    print cv([10, 4, 12, 15, 20, 5])

