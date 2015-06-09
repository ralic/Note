# coding=utf-8
# 使用密匙连接远程
import os
import paramiko
from ConfigParser import ConfigParser
config = ConfigParser()
config.read("config.ini")
HOST = "52.68.177.80"
PORT = int(config.get("EC2", "port"))
USERNAME = config.get("EC2", "username")


class SSHSpiderManager(object):
    def __init__(self, host=HOST, port=PORT, username=USERNAME, password=None, key_filename=None):
        self.host = host
        self.port = port
        self.username = username
        self.keyfilename = key_filename
        self.password = password

    def init_sshclient(self):
        client = paramiko.SSHClient()
        if self.keyfilename is not None:
            client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.host, self.port, self.username, self.password, key_filename=self.keyfilename)
        return client


ssh = SSHSpiderManager(key_filename="viscovery.pem")
client = ssh.init_sshclient()
# 执行命令
command = raw_input()
# chan = client.invoke_shell()
while command != "what a fucking day":
    command.replace("\r\n", "")
    # stdin, stdout, stderr = chan.exec_command(command)
    # print stdin.read()
    # print stdout.read()
    # print stderr.read()
    command = raw_input()
client.close()