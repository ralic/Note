# -*- coding: utf-8 -*-

# Scrapy settings for tenancy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tenancy'

SPIDER_MODULES = ['tenancy.spiders']
NEWSPIDER_MODULE = 'tenancy.spiders'
ITEM_PIPELINES = {
    "tenancy.pipelines.TenancyPipeline": 456,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tenancy (+http://www.yourdomain.com)'
