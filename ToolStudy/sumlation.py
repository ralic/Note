# coding=utf-8
# 模拟发送请求
import requests
import json
import time
keywords = ["Kindle", "Robot"]

def send_simple_request(url="http://127.0.0.1:5000/index"):
    r = requests.get(url, params={"keyword": "牛奶", "count": "5"})
    print "=====>", r.url
    print r.content



numtrial = 10000
print "start to test..."
success = 0
for num in range(numtrial):
    resutl = send_simple_request()
    print "request: %d" % (success + 1)
    success += 1