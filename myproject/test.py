# -*- coding: utf8 -*-

import urlparse


def parseargv(urlstr):
    urlstr = urlparse.urlparse(urlparse.unquote(urlstr)).query
    print urlstr.split("&")
    return {argv.split("=")[0] :argv.split("=")[1] for argv in urlstr.split('&') if argv.find("=") >= 0}



if __name__ == "__main__":
    urlstr = "https://account.guokr.com/sign_in/?success=https%3A%2F%2Faccount.guokr.com%2Foauth2%2Fauthorize%2F%3Fclient_id%3D32353%26redirect_uri%3Dhttp%253A%252F%252Fwww.guokr.com%252Fsso%252F%253Flazy%253Dy%2526rid%253D1900770834%2526success%253Dhttp%25253A%25252F%25252Fwww.guokr.com%25252F%26response_type%3Dcode%26state%3D47f687cada7432a8ff5cf742ce11967d96048a40fc084491ba16da003d65ae5f--1422926530%26suppress_prompt%3D1"
    print parseargv(urlstr)
