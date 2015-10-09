# coding=utf-8
"""
A decorator itself is a callable that returns a callable。
Decorator Nesting:
    @A
    @B
    @C
    def f(...):
        ...
runs the same as the following:
    def f(...):
        ...
    f = A(B(C(f)))

Decorator Arguments：
    @decorator(A, B)
    def F(arg):
        ...
    runs the same as the following:
    def F(arg):
        ...
    F = decorator(A, B)(F) # Rebind F to result of decorator's return value


"""


# 1.Function Decorators
def decorator(func):
    def wrapper(*args, **kwargs):
        print "start", args, kwargs
        f = func(*args, **kwargs)
        print f
        print "end"
        return f
    return wrapper


@decorator
def ft(a, b):      # ft = decprator(ft)(a, b)
    return a+b


# 2. tracing calls
class tracer(object):
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print 'call %s to %s' % (self.calls, self.func.__name__)
        self.func(*args, **kwargs)

@tracer
def spam(a, b, c):
    print sum([a, b, c])


spam(1, 2, 3)
spam(2, 3, 4)
spam(1, 1, 1)
print spam
