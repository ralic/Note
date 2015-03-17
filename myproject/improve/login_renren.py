# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib

url = "https://account.guokr.com/sign_in/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'}
class Login(object):

    def __init__(self, name="", password=""):
        self.name = name
        self.password = password
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def login(self):
        postdata = urllib.urlencode({"csrf_token": "1422521126.91##2a2e390182ee5017598776447ccd8c1936b60ed7",
                                     "form_email": "383274560@qq.com", "form_password": "yzbrqu1314"})
        req = urllib2.Request(url, postdata, headers=headers)
        response = urllib2.urlopen(req)
        self.opener = self.opener.open(req)
        for key, value in self.opener:
            print key, value

user = Login()
user.login()