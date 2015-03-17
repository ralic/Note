# -*- coding: utf-8 -*-

import string


# map(...)
#    map(function, sequence[, sequence, ...]) -> list
#    对序列中的每个元素执行函数（依次取所有序列同一位置的元素放入函数执行）
#    Return a 列表 of the results of applying the function to the items of
#    the argument sequence(s).  If more than one sequence is given, the
#    function is called with an argument list consisting of the corresponding
#    item of each sequence, substituting None for missing values when not all
#    sequences have the same length.  If the function is None, return a list of
#    the items of the sequence (or a list of tuples if more than one sequence).

# filter(...)
#     filter(function or None, sequence) -> list, tuple, or string
#     序列中每个元素执相应行函数， 挑出结果为真的返回
#     Return those items of sequence for which function(item) is true.  If
#     function is None, return the items that are true.  If sequence is a tuple
#     or string, return the same type, else return a list.
lambda_list = [
    lambda x: x > 0,
    lambda x: x in string.ascii_letters
]
print filter(lambda_list[0], range(-9, 5))
print filter(lambda_list[1], "asdfg9487hji123")

#   reduce(...)
#    reduce(function, sequence[, initial]) -> value
#    自己看,比如计算阶乘啥的
#    Apply a function of two arguments cumulatively to the items of a sequence,
#    from left to right, so as to reduce the sequence to a single value.
#    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
#    of the sequence in the calculation, and serves as a default when the
#    sequence is empty.


def myreduce(func, sequence):
    """功能和reduce一样"""
    start = sequence[0]
    for nxt in sequence[1:]:
        start = func(start, nxt)
    return start

print reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print myreduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

