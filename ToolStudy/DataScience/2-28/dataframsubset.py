# coding=utf-8
import pandas as pd

'''
You can think of a DataFrame as a group of Series that share an index.
This makes it easy to select specific columns that you want from the 
DataFrame. 

Also a couple pointers:
1) Selecting a single column from the DataFrame will return a Series  ,选取单行返回Series
2) Selecting multiple columns from the DataFrame will return a DataFrame， 选取多行DataFrame

'''
# Change False to True to see Series indexing in action
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print football['year']
    print ''
    print football.year  # shorthand for football['year']
    print ''
    print football[['year', 'wins', 'losses']]

'''
选取行的若干种方法
Row selection can be done through multiple ways.

Some of the basic and common methods are:
   1) Slicing
   2) An individual index (through the functions iloc or loc)
   3) Boolean indexing

You can also combine multiple selection requirements through boolean
operators like & (and) or | (or)
'''
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data, index=["A", "B", "C", "D", "E", "F", "G", "H"])
    # 位置选取
    print football.iloc[[0]]
    print ""
    # 标签选取,即通过行名称来选取
    print football.loc["A":"D"]
    print ""
    print football[3:5]     # 通过分片，选取多行
    print ""
    print football[football.wins > 10]  # 过滤出wins值>10的行
    print ""
    print football[(football.wins > 10) & (football.team == "Packers")]
