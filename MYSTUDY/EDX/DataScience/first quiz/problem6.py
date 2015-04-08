# coding=utf-8
import pylab
import random

# 白球
A = [0 for i in range(500)]
# 红球
B = [1 for j in range(500)]
BALLS = A + B
random.shuffle(BALLS)


def LV():
    """
    模拟从袋中（500个白球、500个黑球）第一次取到白球要取的次数
    一旦取到白球，就结束，否则继续取球
    """
    balls = BALLS[:]
    num = 0
    while len(balls) > 0:
        print len(balls), "------"
        num += 1
        ball = balls.pop(random.randrange(0, len(balls)-1))
        print ball
        if ball == 0:
            return num + 1
    else:
        pass


def MV():
    balls = BALLS[:]
    num = 0
    localtions = random.randrange(0, 1000)
    while True:
        localtions = localtions % 1000
        num += 1
        if balls[localtions] == 0:
            return num
        else:
            localtions += 1
            continue

def lv_solution():
    histogram = [0 for i in range(1, 1000)]  # intialize the list to be all zeros
    for i in range(1000):
        result = LV()
        histogram[result] += 1
    pylab.plot(range(1, 1000), histogram)

def mv_solution():
    histogram = [0 for i in range(1, 1000)]  # intialize the list to be all zeros
    for i in range(1000):
        result = MV()
        histogram[result] += 1
    pylab.plot(range(1, 1000), histogram)

mv_solution()
pylab.show()
