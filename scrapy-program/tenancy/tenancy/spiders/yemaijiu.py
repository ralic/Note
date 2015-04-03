from scrapy.spider import Spider
from scrapy.http import Request


class YemaiSpider(Spider):
    name = "yemai"
    # http://list.yesmywine.com/z2-b4-e1-d3f-r3-p
    start_urls = ["http://list.yesmywine.com/z2-b4-e1-d3f-r3-p" + str(num) for num in range(1, 7)]

    def __init__(self, **kwargs):
        super(YemaiSpider, self).__init__(**kwargs)
        self.CACULATE = {}
        self.count = 0

    def make_requests_from_url(self, url):
        return Request(url, callback=self.parse_url)

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse_url(self, response):
        good_urls = response.xpath("//a[@class='pname']//@href").extract()
        for url in good_urls:
            print "request for ...%s " % url
            yield Request(url, callback=self.parse)

    def parse(self, response):
        try:
            imglen = len(response.xpath("//ul[@id='image_list']//li").extract())
            print "url is %s \n length is %d " % (response.url, imglen)
        except:
            print "agjhdsjklahsgAAAAAAAAAAAAAAAAAAAAAAAA"
        else:
            self.CACULATE[imglen] = self.CACULATE.setdefault(imglen, 0) + 1
            return []