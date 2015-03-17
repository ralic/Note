# -*- coding: utf8 -*-
#
# 抓取知乎日报的内容

import urllib
import urllib2
from bs4 import BeautifulSoup

BASEPATH = r"D://"
HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36"
}


def getallurl(initial_url):
    """
    initial_url = "http://daily.zhihu.com/"
    """
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36"
    headers = {"User-Agent": user_agent}
    req = urllib2.Request(initial_url, headers=HEADER)
    response = urllib2.urlopen(req)
    data = response.read()
    soup = BeautifulSoup(data)
    urllist = [url.find("a")["href"] for url in soup.find_all("div", class_="box")]
    print urllist
    return urllist


def parse_data(soup):
    result_dict = {}
    result_dict["title"] = soup.title.get_text()
    try:
        result_dict["author"] = soup.find("span", class_="author").get_text(strip=True)
    except:
        pass
    try:
        result_dict["bio"] = soup.find("span", class_="bio").get_text(strip=True)
    except:
        result_dict["bio"] = u"匿名用户"
    result_dict["content"] = soup.find("div", class_="content").get_text(strip=True)
    return result_dict


def download(urllist):
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36"
    headers = {"User-Agent": user_agent}
    for url in urllist:
        req = urllib2.Request(url, headers=HEADER)
        response = urllib2.urlopen(req)
        data = response.read()
        soup = BeautifulSoup(data)
        result = parse_data(soup)
        f = open(BASEPATH+result["title"]+".html", "w")
        lines = ["%s : %s \n" % (key.encode("utf8"), value.encode("utf8")) for key, value in result.items()
                 if len(result) >= 4]

        f.write("".join(lines))
        f.close()
    print "all done"


def main():
    download(getallurl("http://daily.zhihu.com/"))

if __name__ == "__main__":
    main()