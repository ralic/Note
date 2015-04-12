# coding=utf-8
# 利用join等待进程， 直到所有子进程结束才停止父进程。注意设置timeout
import multiprocessing
import time


def daemon():
    p = multiprocessing.current_process()
    print "starting:", p.name, p.pid
    time.sleep(2)
    print "exiting...", p.name, p.pid


def non_daemon():
    p = multiprocessing.current_process()
    print "starting:",  p.name, p.pid
    print "exiting...", p.name, p.pid


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True   # 是否为守护进程

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
    d.join(1)   # 超时值小于守护进程睡眠值，故守护进程依然alive
    print d.is_alive()
    n.join(1)