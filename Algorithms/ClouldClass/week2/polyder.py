# coding=utf-8
# 多项式求导


def polyder(indexnum, factor):
    if indexnum == 0 or factor == 0:
        return 0, 0
    else:
        return factor * indexnum, factor - 1


def add_index_by_factor(result_list, index, factor):
    local = result_list.index(factor)
    result_list[local-1] += index


def print_order_by_factor(result_list, factor_list):
    result_str = []
    factor_list.sort(reverse=True)
    for local in factor_list:
        index = result_list.index(local)
        result_str.append("%s %s" % (result_list[index - 1], result_list[index]))
    print " ".join(result_str)


def main():
    inputs = raw_input()
    numbers = [int(i) for i in inputs.split(' ')]
    if len(numbers) % 2 != 0:
        return
    result_list = []
    exist_factor = []
    for i in range(0, len(numbers)-1, 2):
        index, factor = polyder(numbers[i], numbers[i+1])
        if index == factor and factor == 0:
            continue
        if factor in exist_factor:
            add_index_by_factor(result_list, index, factor)
        else:
            result_list.extend([index, factor])
            exist_factor.append(factor)
    print_order_by_factor(result_list, exist_factor)


# inputs = raw_input().split()
#
# if len(inputs) == 2 and inputs[1] == '0':
#     print 0, 0
# else:
#     result_list = []
#     for i in range(0, len(inputs)-1, 2):
#         if inputs[i+1] != '0' and inputs[i] != '0':
#             index = int(inputs[i]) * int(inputs[i+1])
#             factor = int(inputs[i+1])-1
#             result_list.append("%s %s" % (index, factor))
#     print " ".join(result_list)