# coding=utf-8
# 创建进程池，实现多进程
from multiprocessing import Pool
import os
import time
import random
import asyncore


def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    # random.random() 返回(0-1)dsa
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    # 创建进程池
    p = Pool()
    print p._cache
    for i in range(9):
        # 添加进程至进程池
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    # 关闭进程池
    p.close()
    p.join()
    print 'All subprocesses done.'