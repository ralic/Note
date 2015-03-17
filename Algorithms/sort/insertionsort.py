# coding=utf-8
# 插入排序， 时间复杂度O(n2)


# 从第2个元素开始循环
# 记录当前元素的值
# 相邻元素比较，小元素往相应方向移动（本例为向左）
def insertionsort(alist):
    for location in range(1, len(alist)):
        currentvalue = alist[location]      # 待排序的值
        postion = location                  # 初始位置
        while postion > 0 and alist[postion - 1] > currentvalue:    #
            alist[postion] = alist[postion-1]
            postion -= 1
        alist[postion] = currentvalue

if __name__ == '__main__':
    testlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionsort(testlist)
    print testlist