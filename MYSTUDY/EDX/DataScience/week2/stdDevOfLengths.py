# coding=utf-8
# 求标准差
def stdDevOfLengths(L):
    import math
    if not L:
        return float('NaN')
    numlist = [len(num) for num in L]
    length = len(numlist)
    mean = sum(numlist)/float(length)
    dev = sum([(num - mean) ** 2 for num in numlist])/float(length)
    return math.sqrt(dev)

if __name__ == '__main__':
    print stdDevOfLengths(['a', 'z', 'p'])
    print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
