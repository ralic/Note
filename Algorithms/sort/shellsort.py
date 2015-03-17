# coding=utf-8


# 制定好分组的规则
def shellsort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapinsertionsort(alist, startposition, sublistcount)
        print "After increments of size", sublistcount, 'The list is', alist
        sublistcount //= 2


# 对每个分好的组进行插入排序
def gapinsertionsort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        postion = i
        while postion >= gap and alist[postion - gap] > currentvalue:
            alist[postion] = alist[postion - gap]
            postion -= gap
        alist[postion] = currentvalue

if __name__ == '__main__':
    testlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellsort(testlist)
    print testlist