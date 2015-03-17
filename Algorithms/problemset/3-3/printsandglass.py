# coding=utf-8


#    本题要求你写个程序把给定的符号打印成沙漏的形状。例如给定17个“*”，要求按下列格式打印
#
#    *****
#     ***
#      *
#     ***
#    *****
#    所谓“沙漏形状”，是指每行输出奇数个符号；各行符号中心对齐；相邻两行符号数差2；符号数先从大到小顺序递减到1，再从小到大顺序递增；首尾符号数相等。
#
#    给定任意N个符号，不一定能正好组成一个沙漏。要求打印出的沙漏能用掉尽可能多的符号。
#
#    输入格式：
#
#    输入在一行给出1个正整数N（<=1000）和一个符号，中间以空格分隔。
#
#    输出格式：
#
#    首先打印出由给定符号组成的最大的沙漏形状，最后在一行中输出剩下没用掉的符号数。
#
#    输入样例：
#    19 *
#    输出样例：
#    *****
#     ***
#      *
#     ***
#    *****
#    2
def printsandglass(star, symobo='*'):
    if star < 1:
        return
    rest_of_star = star - 1
    level = 2
    high = 1
    while True:
        level_stars = (2 * level - 1) * 2
        if rest_of_star - level_stars >= 0:
            rest_of_star -= level_stars
            level += 1
            high += 2
        else:
            break
    starlist = [' '*(level-i-1) + (2*i-1)*symobo for i in range(1, level)]
    final_list = starlist[::-1] + starlist[1:]
    print "\n".join(final_list)
    print rest_of_star

if __name__ == '__main__':
    printsandglass(19)

if __name__ == '__main__':
    print printsandglass(19)