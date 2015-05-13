# coding=utf-8
# 有序字典
from collections import OrderedDict

orderdict = OrderedDict()

# 有序字典对有序的列表进行去重
def unique(integers):
    # 将可迭代对象的所有值作为key，他们的值都为value
    return list(OrderedDict.fromkeys(integers, value=None))


print unique([1, 1, 2, 3, 4, 2, 2, 2])