# coding=utf-8
import pylab
import numpy

def loadfile():
    infile = open('julyTemps.txt', 'r')
    high = []
    low = []
    for line in infile:
        fields = line.split(' ')
        if len(fields) != 3 or fields[0] == 'Boston' or fields[0] == 'Day':
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return low, high


# 绘制温差图形，接收两个列表参数，分别为每天的最低温度和每天最高温度
# 设置图形的标题，x、y轴的描述label
# 显示绘制的图形
def produceplot(lowtemps, hightemps):
    pylab.title("Day by Day Ranges in Temperature in Boston in July 2012")
    pylab.xlabel("Days")
    pylab.ylabel("Temperature Range")
    difftemp = [temp[1] - temp[0] for temp in zip(lowtemps, hightemps)]     # 计算每天的温差
    pylab.plot(range(1, 32), difftemp)
    pylab.show()


def produceplot_by_numpy(lowtemps, hightemps):
    pylab.title("Day by Day Ranges in Temperature in Boston in July 2012")
    pylab.xlabel("Days")
    pylab.ylabel("Temperature Range")
    pylab.plot(range(1, 32), (numpy.array(hightemps) - numpy.array(lowtemps)))
    pylab.show()


if __name__ == '__main__':
    result = loadfile()
    produceplot(result[0], result[1])
    produceplot_by_numpy(result[0], result[1])