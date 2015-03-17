# coding=utf-8
# 二分查找(首先列表必须是有序的)


#   Tabular Analysis for a Binary Search
#   Comparisons 	Approximate Number of Items Left
#       1	                n/2
#       2	                n/4
#       3	                n/8
#       ...
#       i	                n/2i
# n/2^i = 1  故i = log n  所以时间复杂度为O（log n）
def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if alist[middle] == item:
            found = True
        else:
            if item > alist[middle]:
                first = middle + 1
            else:
                last = middle - 1
    return found


# 使用递归实现二分搜索（list复制造成额外的开销）
def binary_search_recursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            # 列表的复制造成额外的开销，故这种递归的方式时间复杂度不是O(log n)
            if item > alist[midpoint]:
                return binary_search_recursive(alist[midpoint+1:], item)
            else:
                # 注意不是midpoint-1
                return binary_search_recursive(alist[:midpoint], item)


# 使用递归实现二分搜索（无list复制的开销）
def binary_search_recursive2(alist, item, first, last):
    if first > last:
        return False
    else:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item > alist[midpoint]:
                return binary_search_recursive2(alist, item, midpoint + 1, last)
            else:
                # 注意不是midpoint-1
                return binary_search_recursive2(alist, item, first, midpoint - 1)

if __name__ == '__main__':
    testlist = [1, 2, 3, 4, 5, 6, 7, 8]
    print binary_search(testlist, 1)
    print binary_search(testlist, 10)
    print binary_search_recursive(testlist, 1)
    print binary_search_recursive(testlist, 10)
    print binary_search_recursive2(testlist, 1, 0, len(testlist) - 1)
    print binary_search_recursive2(testlist, 10, 0, len(testlist) - 1)