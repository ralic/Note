# coding=utf-8
# 求最大子序列和


# 常规方法
def maxsubseqsum(alist):
    maxsum = 0
    n = len(alist)
    for i in range(n):
        thissum = 0
        for j in range(i, n):
            thissum += alist[j]
            if thissum > maxsum:
                maxsum = thissum
    return maxsum


# 在线处理算法
def maxsubseqsum2(alist):
    thissum = maxsum = 0
    for i in alist:
        thissum += i
        if thissum > maxsum:
            maxsum = thissum
        if thissum < 0:
            thissum = 0
    return maxsum


# 求最大子序列，以及该最大子序列的开头与结尾
# 输出最大和、最大连续子序列的第一个和最后一个元 素，中间用空格分隔。
# 如果最大连续子序列不唯一，则输出序号i和j最小的那个（如输入样例的第2、3组）。
# 若所有元素都是负数，则定义其最大和为0，输出整个序列的首尾元素
def maxsub_first_last(alist):
    maxsum = thissum = 0
    firstindex = 0
    start_end_list = [0, len(alist)-1]
    for lastindex, element in enumerate(alist):
        thissum += element
        if thissum > maxsum:
            maxsum = thissum
            start_end_list[1] = lastindex
        if thissum == maxsum:
            # 若序号比较大，则选择较小的那个
            if start_end_list[1] >= lastindex:
                start_end_list[0] = firstindex
                start_end_list[1] = lastindex
        if thissum < 0:
            firstindex = lastindex + 1
            thissum = 0
    return maxsum, alist[start_end_list[0]], alist[start_end_list[1]]

if __name__ == '__main__':
    # print maxsubseqsum([1, 2, -3, 5])
    # print maxsubseqsum2([1, 2, -3, 5])
    print "%d %d %d" % maxsub_first_last([-10, 1, 2, 3, 4, -5, -23, 3, 7, -21])
    print "%d %d %d" % maxsub_first_last([-2, 11, -4, 13, -5, -2])
    print "%d %d %d" % maxsub_first_last([-1, 0, -2])
    print "%d %d %d" % maxsub_first_last([5, -8, 3, 2, 5, 0])
    print "%d %d %d" % maxsub_first_last([-1, -5, -2])
    print "%d %d %d" % maxsub_first_last([10])
