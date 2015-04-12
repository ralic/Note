# coding=utf-8
import multiprocessing
import multiprocessing_import_worker

def worker(num):
    print "Worker %d" % num
    return


def test_worker():
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()


def test_worker_protect():
    # 新进程启动要求子进程能够导入包含目标函数的脚本
    # 故将目标函数保存到一个独立模块，确保模块导入不会在各个子进程中递归运行
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=multiprocessing_import_worker.worker, args=(i, ))
        jobs.append(p)
        p.start()
if __name__ == '__main__':
    test_worker()
    test_worker_protect()