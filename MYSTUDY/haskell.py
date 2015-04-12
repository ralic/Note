# coding=utf-8
# 练习用python实现haskell的函数
import functools

# succ 数值+1
succ = lambda x: x + 1


# head 取第一个元素
head = lambda lst: lst[0]

# last 取最后一个元素
last = lambda lst: lst[-1]


# tail 去掉第一个元素的列表
tail = lambda lst: lst[1:]

# init 去掉最后一个元素的列表
init = lambda lst: lst[:-1]

# null 判断列表为空
null = lambda lst: lst == []

# take
take = lambda num, lst: lst[:num]


if __name__ == '__main__':
    print "succ 1, 2, 100:", succ(1), succ(2), succ(100)
    print "head from [1, 2, 3, 4, 5]:", head([1, 2, 3, 4, 5])
    print "last from [1, 2, 3, 4, 5]:", last([1, 2, 3, 4, 5])
    print "tail from [1, 2, 3, 4, 5]:", tail([1, 2, 3, 4, 5])
    print "init from [1, 2, 3, 4, 5]:", init([1, 2, 3, 4, 5])
    print "take first three numbers from [1, 2, 3, 4, 5]:", take(3, [1, 2, 3, 4, 5])
    print "null:", null([])


