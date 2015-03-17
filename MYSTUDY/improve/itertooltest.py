# coding=utf-8
import itertools

"""无穷循环"""


# count 从10开始,每次递增2
def mycount(start=0, increase=1):
    while True:
        yield start
        start += increase
print "Step1: Test count......"
for i in mycount(10, 2):
    print i,
    if i >= 100:
        print
        break
for i in itertools.count(10, 2):
    print i,
    if i >= 100:
        print
        break


# 序列元素重复
def mycycle(sequence):
    while True:
        for s in sequence:
            yield s

# for i in itertools.cycle([1, 2, 3]):
#     print i

# 重复一个元素n次
# for i in itertools.repeat(10, 10):
#     print i

print map(pow, [1,2,3], [1,2,3])
print itertools.imap(pow, [1,2,3], [1,2,3])

