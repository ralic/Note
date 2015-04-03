from lxml import etree
import requests
import threading
from multiprocessing import Process

start_urls = ["http://list.yesmywine.com/z2-c1-" + str(num) for num in xrange(1, 129)]


class RunSpiderThread(threading.Thread):
    def __init__(self, urls):
        threading.Thread.__init__(self)
        self.urls = urls
        self.counts = 0
        self.res = {}

    def run(self):
        for req in send_request(self.urls):
            self.res[req] = self.res.setdefault(req, 0) + 1

    def getresult(self):
        return self.res

    def getcounts(self):
        return self.counts

CACULATE = {}


def send_request(urllist):
    for url in urllist:
        r = requests.get(url)
        print "request for ...%s " % url
        print "status code is:", r.status_code
        try:
            body = etree.HTML(r.content)
            good_urls = body.xpath("//a[@class='pname']//@href")
            print good_urls
            for goodurl in good_urls:
                yield get_have_surface(goodurl)
        except:
            print "error...."



def get_have_surface(url):
    r = requests.get(url)
    try:
        body = etree.HTML(r.content)
        imglen = len(body.xpath("//ul[@id='image_list']//li"))
        print "url is %s \n length is %d " % (url, imglen)
    except:
        return 0
    else:
        return imglen


def main():
    print "Start to carwl ...."
    urls = [["http://list.yesmywine.com/z2-c1-" + str(num) for num in range(start[0], start[1])]
            for start in [(1, 15), (15, 30), (30, 45), (45, 60), (60, 75),  (75, 90), (105, 120), (121, 129)]]
    threads = []
    for url_thread in urls:
        t = RunSpiderThread(url_thread)
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=3)
    for thread in threads:
        dct = thread.getresult()
        print dct


if __name__ == '__main__':
    for num in send_request(start_urls):
        CACULATE[num] = CACULATE.setdefault(num, 0) + 1
    print CACULATE
