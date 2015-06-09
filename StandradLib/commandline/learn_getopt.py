# coding=utf-8
import getopt
import sys

"""
 getopt 参数一: 待解析参数序列
        参数二：单字符选项，若选项需要参数，则相应字符会有一个冒号
        参数三：长格式选项，若选项需要参数，则相应字符会有个等号

"""

tp = "url"
name = "default"
print "ARGV         :", sys.argv[1:]

options, remainder = getopt.getopt(sys.argv[1:], 't:n:', ['type=', 'name='])
for opt, arg in options:
    if opt in ('-n', '--name'):
        name = arg
    elif opt in ('-t', '--type'):
        tp = arg

print "type:", tp
print "name :", name
print "remainder :", remainder