# coding=utf-8

# 选择排序
# 1、遍历每个元素
# 2、将当前元素与其后面的元素依次比较，得到比较过程中最大值的位置,
# 3、交换当前元素与最大元素的位置，重复步骤2
# 时间复杂度O(n2)


# 从左往右的顺序进行排序（或者可以从右到左）
def selectsort(alist):
    for fillslot in range(0, len(alist)):
        max_value_position = fillslot
        for location in range(fillslot + 1, len(alist)):
            if alist[max_value_position] > alist[location]:
                max_value_position = location
        alist[fillslot], alist[max_value_position] = alist[max_value_position], alist[fillslot]


if __name__ == '__main__':
    testlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectsort(testlist)
    print testlist