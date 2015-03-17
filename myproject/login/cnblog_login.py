# coding=utf-8
import urllib2
import cookielib
from bs4 import BeautifulSoup
import urllib

header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"492",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"__gads=ID=489724ae0d2df86e:T=1422861456:S=ALNI_Mbon_N8yKZLbKsf9nEygeYSQhC9SQ; _ga=GA1.2.337726467.1422861455; __utma=215813774.337726467.1422861455.1422864672.1422864672.1; __utmb=215813774.8.10.1422864672; __utmc=215813774; __utmz=215813774.1422864672.1.1.utmcsr=passport.cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/login.aspx; SERVERID=73ea7682c79ff5c414f1e6047449c5c1|1422865849|1422864671; .DottextCookie=D2712597BB6E6808763513B6E45C58E2655D4A2C4350581C852426A4346DB09F999EE13ABBD2F5D39FE8605052CE09C6E819A46A3C477B21C829054D3CF71D8DC19124C16E0E2C60E8DE26C7C6E5F192BCE24994696458BBF03A70D7B5778582AD4A0B644288023564587171713A5455403D233D",
    "Host":"home.cnblogs.com",
    "Origin":"http://passport.cnblogs.com",
    "RA-Sid":"655135A8-20150114-105635-81a574-ed620f",
    "RA-Ver":"2.8.7",
}
data = {
    "__EVENTTARGET": "",
    "__EVENTARGUMENT":"",
    "__VIEWSTATE":"/wEPDwUKLTM1MjEzOTU2MGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFC2Noa1JlbWVtYmVy4b/ZXiH+8FthXlmKpjSEgi7XBNU=",
    "__VIEWSTATEGENERATOR":"C2EE9ABB",
    "__EVENTVALIDATION":"/wEdAAUIqCk3Gcmu25zI9fQWqoC7hI6Xi65hwcQ8/QoQCF8JIahXufbhIqPmwKf992GTkd0wq1PKp6+/1yNGng6H71Uxop4oRunf14dz2Zt2+QKDEM3sbzJLySdZoy08+/dzW8VF2on0",
    "tbUserName":"loveyui1314",
    "tbPassword":"_wx1314hij",
    "btnLogin":"登 录",
    "txtReturnUrl": "http://home.cnblogs.com/"
}
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
# 使用data登陆
# r = opener.open("http://passport.cnblogs.com/login.aspx", urllib.urlencode(data))
# print cj
#
# html = urllib2.urlopen("http://home.cnblogs.com/set/account/").read()
# soup = BeautifulSoup(html)
# print soup.prettify()

# 使用cookie登陆
req = urllib2.Request("http://home.cnblogs.com/", headers=header)
cj.add_cookie_header(req)
print cj

