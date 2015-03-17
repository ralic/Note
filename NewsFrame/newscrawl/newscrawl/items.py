# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewscrawlItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    cate = scrapy.Field()
    label = scrapy.Field()
    url = scrapy.Field()
    shortcut = scrapy.Field()
