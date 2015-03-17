# coding=utf-8
# 行列的处理
import pandas
import sys

print "Python version" + sys.version
print "Pandas version" + pandas.__version__

d = range(10)
df = pandas.DataFrame(d)    # 创建一个数据框(只有一列)
df.columns = ['Rev']        # 添加列名
df["NewCol"] = 5            # 添加新列
df['NewCol'] += 1           # 更改新列的值
del df['NewCol']            # 删除对应列名的列
df['test'] = 3
df['col'] = df['Rev']
i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df.index = i                # 添加行名
# 取行
print df.loc['a']          # 根据行名取对应行
print df.loc['a':'c']      # 取多行
print df.iloc[0]           # 根据行索引取对应行
print df.iloc[0:3]         # 根据行索引取多行
# 取列
print df['Rev']           # 取单列
print df[['Rev', 'test']]   # 取多列
print df['Rev'][0:3]        # 取单列前几行
print df[['Rev', 'test']][:3]   # 取多列前几行
print df.tail()
