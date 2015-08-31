# coding=utf-8
import requests
import re
"""
staticpage=http%3A%2F%2Fyun.baidu.com%2Fchres%2Fstatic%2Fjs%2Fpass_v3_jump.html&charset=utf-8&token=e8ad9ec4a83f8e2ad24b87c072bba130&tpl=yun&subpro=&apiver=v3&tt=1429754589415&codestring=&safeflg=0&u=http%3A%2F%2Fyun.baidu.com%2F&isPhone=&quick_user=0&logintype=basicLogin&logLoginType=pc_loginBasic&idc=&loginmerge=true&username=loveyui1314&password=B%2FeO8LjnZWdYoOQHVuOspBWxpTA0Kj2jGxmuaKgMCkuOJQRtA9QtqoAVAmXMSXg9TMn0fIyHQ1ruPzWymlFp%2B%2BqlnGeH3pUb8E7Rw%2FdSTonwJyWDtifK1WqNweWG8KZHwiYO6dH9AyaqExiCvqE73lxhW4MFDE04LNQILL7WAgs%3D&verifycode=&rsakey=euh9pbqBdnbxkV49ohKGYcCkXSRMUUKn&crypttype=12&ppui_logintime=183816&callback=parent.bd__pcbs__jae4c0

"""
# https://passport.baidu.com/v2/api/?getapi&apiver=v3   获得token


class LoginBase(object):
    def __init__(self):
        self.session = requests.Session()
        self.headers = {"User-Agent":
                           "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.cookies = {}

    def first_requeset(self):
        first_url = "http://yun.baidu.com/"
        r1 = self.session.get(first_url)
        self.cookies.update(r1.cookies)
        url = "https://passport.baidu.com/v2/api/?getapi&apiver=v3"
        response = self.session.get(url, headers=self.headers, cookies=self.cookies)
        self.cookies.update(r1.cookies)
        token = re.search(r'token.*?: "(.*?)",', response.content).groups()[0]
        return token



if __name__ == '__main__':
    l = LoginBase()
    l.second_request()