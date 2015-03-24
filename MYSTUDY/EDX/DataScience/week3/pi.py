# coding=utf-8
import random, pylab

# set line width
pylab.rcParams['lines.linewidth'] = 6
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
# set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5
# set font size for text
pylab.rcParams['legend.fontsize'] = 20


# 计算标准差（衡量与平均值的接近程度）。标准差又叫均方差，。。
def stdDev(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return (tot / len(X)) ** 0.5


# 往一个2*2的正方形中投针,返回一个估计的pi值
def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in xrange(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        # 圆的面积X^2 + Y^2 = r^2
        if (x * x + y * y) ** 0.5 <= 1.0:
            inCircle += 1
    return 4 * (inCircle / float(numNeedles))


# 获得估计的值
def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    # 进行n次事件后的平均估计值
    curEst = sum(estimates) / len(estimates)
    print 'Est. = ' + str(curEst) + \
          ', Std. dev. = ' + str(round(sDev, 6)) \
          + ', Needles = ' + str(numNeedles)
    return (curEst, sDev)


# 估计pi的值
def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision / 2.0:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst


random.seed(0)
estPi(0.005, 100)

