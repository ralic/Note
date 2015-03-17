# -*- coding: utf8 -*-

import urlparse
import urllib2
import urllib
from bs4 import BeautifulSoup


def parse_query(url_str):
    """分离query中的串"""
    url_str = urlparse.urlparse(urlparse.unquote(url_str)).query
    print urlstr.split("&")
    return {argv.split("=")[0]: argv.split("=")[1] for argv in urlstr.split('&') if argv.find("=") >= 0}


def create_format_header(init_header):
    """将header信息字符串转换成标准格式"""
    headerlist = init_header.strip().split("\n")
    return {var.split(':')[0]: var.split(':')[1] for var in headerlist}


def create_format_cookie(init_cookie):
    """生成cookie字典"""
    cookielist = init_cookie.strip().split(';')
    return {var.split('=')[0]: var.split('=')[1] for var in cookielist}


def create_request(url, data=None, headers={}):
    return urllib2.Request(url, data=data, headers=headers)


def create_bs4(htmlbody):
    return BeautifulSoup(htmlbody)

if __name__ == "__main__":
    urlstr = "https://account.guokr.com/sign_in/?success=https%3A%2F%2Faccount.guokr.com%2Foauth2%2Fauthorize%2F%3Fclient_id%3D32353%26redirect_uri%3Dhttp%253A%252F%252Fwww.guokr.com%252Fsso%252F%253Flazy%253Dy%2526rid%253D1900770834%2526success%253Dhttp%25253A%25252F%25252Fwww.guokr.com%25252F%26response_type%3Dcode%26state%3D47f687cada7432a8ff5cf742ce11967d96048a40fc084491ba16da003d65ae5f--1422926530%26suppress_prompt%3D1"