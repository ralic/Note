import requests
import sys
try:
    username, password = sys.argv[1], sys.argv[2]
except:
    pass
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
}
url = "http://log.viscovery.net.cn/logsystem/Log/Index/verify"
print "create request"
session = requests.Session()
resp = session.post(url, data={"username": "devin", "password": "hij910207"}, headers=header)
print "Create host:"
create_app_resp = session.get("http://log.viscovery.net.cn/logsystem/Log/Spider/spiderhost_create")
print create_app_resp.content