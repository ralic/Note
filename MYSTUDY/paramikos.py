# coding=utf-8
# 使用密匙连接远程
import paramiko
from ConfigParser import ConfigParser
config = ConfigParser()
config.read("config.ini")
HOST = "54.223.214.48"
PORT = int(config.get("EC2", "port"))
USERNAME = config.get("EC2", "username")


class SSHSpiderManager(object):
    def __init__(self, host=HOST, port=PORT, username=USERNAME, password=None, key_filename=None):
        self.host = host
        self.port = port
        self.username = username
        self.keyfilename = key_filename
        self.password = password
        self.client = None

    def init_sshclient(self):
        self.client = paramiko.SSHClient()
        if self.keyfilename is not None:
            self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, self.port, self.username, self.password, key_filename=self.keyfilename)
        return self.client

    def session_task(self, command):
        if not self.client:
            self.init_sshclient()
        session = self.client.get_transport().open_session()
        session.set_combine_stderr(True)
        session.get_pty()
        session.exec_command("sudo -s %s" % command)
        return session.makefile("rb")


ssh = SSHSpiderManager(key_filename="viscovery2015q2ChinaRD3_rsa.pem")


# stdin, stdout, stderr = session.exec_command("sudo /bin/sh /home/ec2-user/es-program/es-python/test.sh")
command = "/bin/sh /home/ec2-user/es-program/es-python/test.sh"
stdout = ssh.session_task(command)
#you have to check if you really need to send password here
# stdin.flush()
for line in stdout.read().splitlines():
    print 'host: %s' % line
# 执行命令
# command = raw_input()
# while command != "what a fucking day":
#     stdin, stdout, stderr = client.exec_command(command)
#     print stdout.read()
#     print stderr.read()
#     command = raw_input()
# client.close()