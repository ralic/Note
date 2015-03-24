# coding=utf-8
# 合并排序

# 递归算法：每次把列表分成两部分，直到列表为空或者只有一个元素为止。
# 对每一个两部分进行排序，然后将其合并成一个。


def mergesort(alist):
    print "Splitting", alist
    if len(alist) > 1:
        mid = len(alist) / 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
        print "Merging ", alist


alist = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
mergesort(alist)
print(alist)
