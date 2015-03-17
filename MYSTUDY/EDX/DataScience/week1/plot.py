# coding=utf-8
import pylab

# 可以通过修改.rc文件，改变默认配置（字体、颜色等）
principal = 10000
interestrate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestrate
pylab.plot(range(years + 1), values, linewidth=30)
pylab.title("%5 Growth, Compounded", fontsize=12)
pylab.xlabel("Years of Compounding", fontsize=24)
pylab.ylabel("Value of Principal  ($)")
pylab.show()