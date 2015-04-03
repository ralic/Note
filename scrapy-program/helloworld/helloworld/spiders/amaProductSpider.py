from scrapy.spider import Spider
from helloworld.items import ProductItem
from scrapy.http import Response
from scrapy.http import Request
def ProductSpider(Spider):
    name = "ama"
    start_urls = ["http://www.amazon.cn/"]
