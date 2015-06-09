# coding=utf-8
import requests
import sys
from bs4 import BeautifulSoup
import time

SERVERID, LOCALIP, IP, STATUS, IMG_STATUS, UPDATETIME, INSTANCEID, STATE, COMMAND = range(9)
try:
    username, password = sys.argv[1], sys.argv[2]
except:
    username, password = ("devin", "hij910207")


class ViscoveryServer(object):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.login_url = "http://log.viscovery.net.cn/logsystem/Log/Index/verify"
        self.server_page_url = "http://log.viscovery.net.cn/logsystem/Log/Spider/spiderhost_list"
        self.create_server_url = "http://log.viscovery.net.cn/logsystem/Log/Spider/spiderhost_create"
        self.chcek_url = "http://log.viscovery.net.cn/logsystem/Log/Spider/spiderhost_check"
        self.delete_url = "http://log.viscovery.net.cn/logsystem/Log/Spider/spiderhost_delete"
        self.session = requests.Session()

    def login_viscovery(self):
        return self.session.post(self.login_url, data={"username": self.user, "password": self.pwd},
                                 headers=self.headers)

    def create_new_server(self):
        self.session.get(self.server_page_url)
        create_header = self.headers.copy()
        create_header.update({"Referer": self.server_page_url,
                              "X-Requested-With": "XMLHttpRequest"})
        create_resp = self.session.get(self.create_server_url, headers=create_header)
        return int(create_resp.text)

    def create_new_server_and_check(self):
        server_id = self.create_new_server()
        self.check_server(server_id)

    def get_useable_ip(self):
        serverlist = []
        resp = self.session.get(self.server_page_url)
        soup = BeautifulSoup(resp.content)
        servers = soup.find_all("tr", {"class", "gradeX"})
        for server in servers:
            serverlist.append([td.get_text(strip=True) for td in server.find_all("td")])
        return serverlist

    def check_server(self, spider_server_id):
        create_header = self.headers.copy()
        create_header.update({"Referer": self.server_page_url,
                              "X-Requested-With": "XMLHttpRequest"})

        return self.session.get(self.chcek_url, params={"id": spider_server_id}, headers=create_header)

    # def delete_server(self, spider_server_id):
    #     self.session.get("http://log.viscovery.net.cn/logsystem/Log/Spider/spiderhost_list")
    #     create_header = self.headers.copy()
    #     create_header.update({"Content-Type": "application/x-www-form-urlencoded",
    #                           "X-Requested-With": "XMLHttpRequest",
    #                           "Referer": "http://log.viscovery.net.cn/logsystem/Log/Spider/spiderhost_list",
    #                           })
    #     resp = self.session.post(self.delete_url, data={"id": spider_server_id})
    #     print resp.content

    def get_a_new_server_ip(self):
        self.login_viscovery()
        spiderid = self.create_new_server()
        time.sleep(5)
        self.check_server(spiderid)
        time.sleep(5)
        serverlist = self.get_useable_ip()
        for server in serverlist:
            if int(server[SERVERID]) == spiderid:
                return server[IP]


if __name__ == '__main__':
    viscovery = ViscoveryServer(username, password)
    loginresp = viscovery.login_viscovery()
    # viscovery.get_a_new_server_ip()
    # viscovery.login_viscovery()
    # servers = viscovery.get_useable_ip()
    # for index, server in enumerate(servers):
    # print server[SERVERID], server[IP]
    # print viscovery.check_server(155).content

