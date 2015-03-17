from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from newscrawl.newscrawl.selectrules import *
import sys

class BossSpider(Spider):
    name = "boss"
    start_urls = []

    def __init__(self, **kwargs):
        super(BossSpider, self).__init__(**kwargs)
        self.domain = get_domain(kwargs.get("domain", None), RULESETTING)

    def start_requests(self):
        if self.domain is not None:
            url_rules = self.domain["URL_RULES"]
            for rule in url_rules:
                urls = produce_urls(rule['initrul'], startpage_num=rule['startpage'], endpage_num=rule["endpage"],
                                    urltype=rule.get("urltype", MID), leftfix=rule.get("leftfix", ""),
                                    order=rule.get("order", True), midfix=rule.get('midfix', ""),
                                    rightfix=rule.get("rightfix", ""))
                self.start_urls.extend(urls)
        if not self.start_urls:
            sys.exit(1)
        for i in self.start_urls:
            print i
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        pass