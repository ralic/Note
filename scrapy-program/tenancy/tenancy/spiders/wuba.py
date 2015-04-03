from tenancy.items import TenancyItem
from scrapy.spider import Spider
from scrapy.http import Request, Response


class WubaSpider(Spider):
    name = 'wuba'
    domain = "http://sh.58.com/"
    start_url = r"http://sh.58.com/chuzu/0/"

    def __init__(self, **kwargs):
        super(WubaSpider, self).__init__(**kwargs)
        self.limit = int(kwargs.get("limit", 1))

    def start_requests(self):
        self.start_urls = [self.start_url + "pn"+str(num) for num in range(1, self.limit + 1)]
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True, callback=self.parse_url)
    """
    title = scrapy.Field()
    detail_url = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()
    short_info = scrapy.Field()
    address = scrapy.Field()
    setting = scrapy.Field()
    telephone = scrapy.Field()
    contact = scrapy.Field()
    lone_detail = scrapy.Field()
    """
    def parse_url(self, response):
        for detail_url, title, price, types in zip(response.xpath("//h1//a[@class='t']//@href").extract(),
                                     response.xpath("//h1//a[@class='t']//text()").extract(),
                                     response.xpath("//b[@class='pri']//text()").extract(),
                                     response.xpath("//span[@class='showroom']//text()").extract()):
            item = TenancyItem()
            item['detail_url'] = detail_url
            item['price'] = price
            item['types'] = types
            yield Request(detail_url, callback=self.parse, meta={"item": item})

    def parse(self, response):
        item = response.meta['item']
        try:
            item['title'] = response.xpath("//h1//text()").extract()[0].strip()
        except:
            pass
        return item
