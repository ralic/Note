__author__ = 'haohua.yao'

import threading


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.res = None

    def run(self):
        self.res = apply(self.func, self.args)

    def getresult(self):
        return self.res
