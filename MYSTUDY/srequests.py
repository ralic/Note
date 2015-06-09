# coding=utf-8
from ConfigParser import ConfigParser
import paramiko
config = ConfigParser()
config.read("config.ini")
host = "54.223.157.200"
port = int(config.get("ROOT", "port"))
username = config.get("ROOT", "username")
password = config.get("ROOT", "password")
client = paramiko.SSHClient()
# client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port, username, password, timeout=5)
# 执行命令
command = raw_input()
while command != "what a fucking day":
    command.replace("\r\n", "")
    stdin, stdout, stderr = client.exec_command(command)
    print stdout.read()
    command = raw_input()
client.close()