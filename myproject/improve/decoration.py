# -*- coding: utf-8 -*-
# @decorator
# def F(arg)          <====>  def F(arg)
#                            F = decorator(F)

def hello(fn):
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print "goodby, %s" % fn.__name__
    return wrapper

# 即等价于 foo = hello（foo）
@hello
def foo():
    print "i am foo"

foo()