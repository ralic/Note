# coding=utf8
import urllib2
import cookielib


class BaseLogin(object):
    def __init__(self):
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))

    def create_request(self, url, data=None, header={}):
        return urllib2.Request(url, data, header)

    def get_body(self, url, data=None, header={}):
        body = urllib2.urlopen((self.create_request(url, data, header)))
        return body


def main():
    pass