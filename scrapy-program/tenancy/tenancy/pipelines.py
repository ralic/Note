# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TenancyPipeline(object):
    def process_item(self, item, spider):
        with open("test.txt", "a") as f:
            for key, value in item.items():
                f.write(key.encode('utf8')+":"+value.encode('utf8') + "\n")
            f.write("\n\n")
        return item
        # return []

    # def close_spider(self, spider):
    #     print "~~~~~"
    #     print spider.CACULATE
    #     no = spider.CACULATE[1] + spider.CACULATE[2]
    #     yes = sum(spider.CACULATE.values()) - no
    #     print "have....", yes
    #     print "have not ...", no
    #     print "~~~~~"