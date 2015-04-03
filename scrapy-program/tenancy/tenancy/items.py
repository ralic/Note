# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TenancyItem(scrapy.Item):
    title = scrapy.Field()
    detail_url = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()
    types = scrapy.Field()
    address = scrapy.Field()
    setting = scrapy.Field()
    telephone = scrapy.Field()
    contact = scrapy.Field()
    lone_detail = scrapy.Field()


class TestItem(scrapy.Item):
    """"""