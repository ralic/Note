# coding=utf-8
import os

from rulesetting import *


def produce_urls(initurl, startpage_num=2, endpage_num=2, urltype=MID, leftfix="", midfix="", rightfix="", order=True):
    """
    url：首页url
    startpage_num, endpage_num： 开始页和结束页
    urltype:表示添加缀的位置（e.g.:xxx.html中xxx的左、中、右部分添加缀）
    leftfix midfix rightfix: 添加的内容
    order:页数为顺序还是倒序
    """
    urllist = [initurl]
    pre, mid = os.path.split(initurl)
    mid, suf = mid.split(".")
    order_num = 1
    # 逆序的话，页数应当-2
    if not order:
        order_num = -1
        endpage_num -= 2
    if urltype == MID:
        for num in range(startpage_num, endpage_num+1, order_num):
            urllist.append(r"%s/%s.%s" % (pre, mid+midfix+str(num), suf))
    elif urltype == RIGHT:
        for num in range(startpage_num, endpage_num+1, order_num):
            urllist.append(r'%s/%s.%s' % (pre, mid, suf+rightfix+str(num)))
    return urllist


def get_domain(domain_name, setting):
    return setting.get(domain_name, None)

if __name__ == '__main__':
    print produce_urls("http://news.cnfol.com/guoneicaijing/index.shtml", 2, 2, midfix='_')
    print produce_urls("http://finance.jrj.com.cn/list/guoneicj.shtml", 2, 2, midfix='-')
    print produce_urls("http://channel.chinanews.com/u/finance/gs.shtml", 2, 2, urltype=RIGHT, rightfix='?pager=')
    print produce_urls("http://finance.huagu.com/cjyw/index.html", 332, 330, midfix='-', order=False)