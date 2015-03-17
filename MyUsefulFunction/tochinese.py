# coding=utf-8
import re

CH = re.compile(u"[\u4e00-\u9fa5]")  # 匹配一个中文字符,注意正则表达式必须前面+u


# 过滤出字符串的中文
def get_chinese(s):
    pattren = re.compile(u"[\u4e00-\u9fa5]")
    return filter(lambda x: re.match(pattren, x), s)


def get_others(s):
    pattern = re.compile(u"[^\u4e00-\u9fa5]")
    return filter(lambda x: re.match(pattern, x), s)


if __name__ == '__main__':
    print get_chinese(u"2013:13:12这csac是45615中vxz文")
    print get_others(u"2013:13:12这cxz是45615中vcx文")
