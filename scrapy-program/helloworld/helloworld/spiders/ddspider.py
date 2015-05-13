from scrapy.spider import Spider


class DDSpider(Spider):
    name = "dd"
    start_urls = ["http://category.dangdang.com/cp01.03.56.01.00.00.html"]

    def parse(self, response):
        for book in response.xpath("//div[@class='inner']//p[@class='name']//a/@title").extract():
            item['title'] = book
            print item, "...."
            yield item