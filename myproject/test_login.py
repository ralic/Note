# -*- coding: utf8 -*-
#
# 知乎模拟登陆：http://www.zhihu.com/login 获得验证码
#
# http://www.zhihu.com/login再次请求，登陆

import cookielib
import urllib
import urllib2
from bs4 import BeautifulSoup

HEADERS = {
    "Accept": "*/*",
    "X-Requested-With":	"XMLHttpRequest",

    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "Host": "www.qhee.com",
    "Origin": "https://www.qhee.com",

}


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
loginurl = "https://www.qhee.com/node/company/standard"

first_req = urllib2.urlopen(loginurl)
# print first_req.read()
print cj
second_req = urllib2.Request("https://www.qhee.com/node/proxy-action/qhee-webapp/action/web/entapply/EntApplyAction/queryByCategory?type=listed_file&pagesize=12",
                             headers=HEADERS)
print urllib2.urlopen(second_req).read()



