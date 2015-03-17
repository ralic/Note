# coding=utf-8
import urllib2
import cookielib
from bs4 import BeautifulSoup
from loginhelper import *

import urllib
HEADER = {
    'Origin': 'http://www.zhihu.com',
    'Host': 'www.zhihu.com',
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36",
    "Cookie": "q_c1=e5bd2bd881504f75be934be2a7fe92ed|1422933004000|1422933004000; _xsrf=2b49376e5e6c841a5fbee064d2ab0b56; __utmt=1; c_c=b84e7964ad0f11e4844b5254291c3363; z_c0='QUFBQUl3OGVBQUFYQUFBQVlRSlZUWi0wLWxTX2lHcnNwbjZFSXZIOEkzcEc5U2czU3ljSDVnPT0=|1423124383|58733dc11896887e440734a5b9f6704e8fe68151; __utma=51854390.1459491904.1422933005.1423119255.1423119255.6; __utmb=51854390.25.9.1423122207441; __utmc=51854390; __utmz=51854390.1423119255.5.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20130912=1^3=entry_date=20130912=1"

}
post_data = create_format_header("""_xsrf:bd83150c8689dcd7e866a86efd93a1e2
email:383274560%40qq.com
password:
rememberme:y""")


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

# # 第一步:获得跳转页面
# login_url = "http://www.zhihu.com/login"
# # 第二步：登陆页面
# print "Create request..."
# req2 = urllib2.Request(login_url, headers=HEADER)
# print "Open page..."
# resp = urllib2.urlopen(req2)
# print "format page..."
# soup2 = BeautifulSoup(resp.read())
# print "cookiejar:", cj
#
# # # 提交表单，打开设置
# result1 = opener.open(req2.url, post_data)
request = urllib2.Request("http://www.zhihu.com/login", headers=HEADER)
request = urllib2.urlopen(request)
request2 = urllib2.urlopen("http://www.zhihu.com/people/yao-xia-mi")
soup = BeautifulSoup(request2.read())
print soup.prettify()


