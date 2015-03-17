# -*- coding: utf8 -*-
__author__ = 'haohua.yao'

import re, urllib2
from bs4 import BeautifulSoup
import chardet

def deletejs(html):
    """去除html页面中的script脚本"""
    pattern = re.compile(r"<script[^>]*?>[\s\S]*?</script>")
    return re.sub(pattern, "",html)


def main(url):
    html = urllib2.urlopen(url).read()
    html = deletejs(html)
    soup = BeautifulSoup(html)
    print url
    print soup.h1.get_text()
    print soup.find("div", class_="info").next_element
    print soup.find("div", class_="info").span.get_text()[3:]
    print soup.find("div", id="ctrlfscont")

if __name__ == "__main__":
    main("http://hk.stcn.com/2014/0429/11382163.shtml")
