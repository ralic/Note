# coding=utf-8
# 顺序查找


# Comparisons Used in a Sequential Search of an Unordered List  (无序列表查找)
# Case	                Best Case	Worst Case	Average Case
# item is present	        1	        n	        n/2
# item is not present	    n	        n	        n
def sequential_search(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


#   able 2: Comparisons Used in Sequential Search of an Ordered List (有序列表查找)
#   Case	                Best Case	Worst Case	Average Case
#   item is present 	        1	        n	        n/2
#   item not present	        1	        n	        n/2
def orderedsequentialsearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1

    return found

if __name__ == '__main__':
    testlist = [1, 2, 3, 4, 5, 6, 7, 9]
    print sequential_search(testlist, 1)
    print sequential_search(testlist, 10)
    print sequential_search(testlist, 6)
    print orderedsequentialsearch(testlist, 1)
    print orderedsequentialsearch(testlist, 9)
    print orderedsequentialsearch(testlist, 11)