# coding=utf-8
# 测试URL基本使用方法
from purl import URL

# 三种初始化方式（通过完整的url字符串， 通过关键字参数，通过）
from_str = URL('https://www.google.com/search?q=testing')
from_kwargs = URL(scheme='https', host='www.google.com', path='/search', query='q=testing')
from_combo = URL('https://www.google.com').path('search')
print type(from_combo), type(from_combo.path("haha"))