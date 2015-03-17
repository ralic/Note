# coding=utf-8
import urllib2
import cookielib
from bs4 import BeautifulSoup
import urlparse
import urllib
Headers = {
    "AllowAutoRedirect": "false",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
}
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

# 第二步：登陆页面
req2 = urllib2.Request("http://www.guokr.com/sso/?suppress_prompt=1&amp;lazy=y&amp;success=http%3A%2F%2Fwww.guokr.com%2F", headers=Headers)
resp = urllib2.urlopen(req2)
soup2 = BeautifulSoup(resp.read())
csrf = soup2.find("input", attrs={'name': 'csrf_token'})["value"]
request_url = resp.url
print csrf
print "cookiejar:", cj

# 提交表单，打开设置
post_data = urllib.urlencode({"csrf_token": csrf, "email": "383274560@qq.com", "password": "*******"})
result1 = opener.open(request_url, post_data)
request = urllib2.Request("http://www.guokr.com/settings/profile/", headers=Headers)
request = urllib2.urlopen(request)
soup = BeautifulSoup(request.read())
print soup.prettify()
