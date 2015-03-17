# coding=utf-8
import urllib2
import cookielib
from bs4 import BeautifulSoup
import urllib
post_data = {
    'rsakey': '0hYazBlVa5EpbVCyexWc4KkdnJsdbOR9',
    'verifycode': '',
    'splogin': 'rate',
    'apiver': 'v3',
    'isPhone': '',
    'tt': '1422870044172',
    'charset': 'utf-8',
    'token': '4a2bfcd4e04f745900223f515c6d090e',
    'ppui_logintime': '233503',
    'subpro': '',
    'username': 'loveyui1314',
    'safeflg': '0',
    'crypttype': '12',
    'staticpage': 'http://www.baidu.com/cache/user/html/v3Jump.html',
    'logLoginType': 'pc_loginDialog',
    'password': 'woxin1314hij',
    'tpl': 'mn',
    'logintype': 'dialogLogin',
    'loginmerge': 'true',
    'callback': 'parent.bd__pcbs__uwk1j7',
    'codestring': '',
    'quick_user': '0',
    'u': 'http://www.baidu.com/',
    'idc': ''
}
#
#
# UBI	fi_PncwhpxZ%7ETaKAeHltgs1LgwmUi3jct5oqPh0G5byzBxR10eW7x2oFSH9Pa0-pROg1xizOSnZrDUsdbHC	Fri, 21-Apr-2023 09:38:39 GMT
# passport.baidu.com	/	否	是
# 已接收	PASSID	d1yaiE	Sun, 02-Feb-2014 09:38:39 GMT	passport.baidu.com	/	否	是

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

req = urllib2.urlopen("http://www.baidu.com")
for index, cookie in enumerate(cj):
    print index, cookie
    print cookie.name

baseurl = "https://passport.baidu.com/v2/api/?login"

request = urllib2.Request(baseurl, urllib.urlencode(post_data))

print urllib2.urlopen(baseurl).read()



