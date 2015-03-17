# coding=utf-8
# 快速排序


def quicksort(alist):
    quicksorthelper(alist, 0, len(alist) - 1)


def quicksorthelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        # 对左边和右边执行相同的选取“基准”排序操作
        quicksorthelper(alist, first, splitpoint - 1)
        quicksorthelper(alist, splitpoint + 1, last)


# 根据“基准”元素，移动元素，最终使左边的元素小于基准元素，右边的元素大于基准元素
def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quicksort(alist)
print(alist)

