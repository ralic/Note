# coding=utf-8
# 多进程demo.

from multiprocessing import Process
import os


def run_proc(name):
    print "Run child process %s (%s)..." % (name, os.getpid())


if __name__ == "__main__":
    print 'Parent process %s.' % os.getpid()
    # 创建子进程：指定进程要执行的函数以及函数相关参数
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    # 启动进程
    p.start()
    # 用于进程同步（即等待所有子进程结束后再往下运行）
    p.join()
    print 'Process end.'