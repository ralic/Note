# coding=utf-8
# 冒泡排序
# Table 1: Comparisons for Each Pass of Bubble Sort
# Pass	    Comparisons
# 1	            n−1
# 2	            n−2
# 3	            n−3
# ...	        ...
# n−1	        1
# O(n2)


def bubblesort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

if __name__ == '__main__':
    testlist = [6, 8, 9, 7, 6, 4, 2]
    bubblesort(testlist)
    print testlist