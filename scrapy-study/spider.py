# coding=utf-8
from scrapy.http import Request


class Spider(object):
    """Base class for scrapy spiders. All spiders must inherit from this
    class.
    """
    # 爬虫的名字
    name = None

    def __init__(self, name=None, **kwargs):
        if name is not None:
            self.name = name
        elif not getattr(self, 'name', None):
            raise ValueError("%s must have a name" % type(self).__name__)
        # 将kwargs中的键值对更新为爬虫的属性
        self.__dict__.update(kwargs)
        if not hasattr(self, 'start_urls'):
            self.start_urls = []

    def __str__(self):
        return "<%s %r at 0x%0x>" % (type(self).__name__, self.name, id(self))

    # 通过yield构造初始的url请求的生成器
    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    # 返回相应url的请求对象
    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True)

    # 子类实现该方法，通常response是HTMLResponse的实例
    def parse(self, response):
        """
        HTMLResponse的方法：
            @property
            def selector(self):
                from scrapy.selector import Selector
                if self._cached_selector is None:
                    self._cached_selector = Selector(self)
                return self._cached_selector

            def xpath(self, query):
                return self.selector.xpath(query)
        由此可以直接通过HTMLResponse的xpath来获取
        """
        raise NotImplementedError


if __name__ == '__main__':
    s = Spider(name=10, a=100)
    print s