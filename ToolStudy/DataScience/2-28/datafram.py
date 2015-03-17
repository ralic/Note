# coding=utf-8
import pandas as pd


'''
The following code is to help you play with the concept of Series in Pandas.

You can think of Series as an one-dimensional object that is similar to
an array, list, or column in a database. By default, it will assign an
index label to each item in the Series ranging from 0 to N, where N is
the number of items in the Series minus one.

Series：    def __init__(self, data=None, index=None, dtype=None, name=None,
                 copy=False, fastpath=False):

基本Series的创建（数据框的列），指定行的名称，取特定行的值，过滤特定值。
'''
# Change False to True to create a Series object
if True:
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
    print series

'''
You can also manually assign indices to the items in the Series when
creating the series
'''

# Change False to True to see custom index in action， index指定对应的值的名称（即每一行的名称）
if True:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print series

'''
You can use index to select specific items from the Series
'''
print
# Change False to True to see Series indexing in action， 通过index名字选则特定的行，
if True:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print series['Instructor']
    print ""
    print series[['Instructor', 'Curriculum Manager', 'Course Number']]     # 注意选择多行时需要用列表

'''
You can also use boolean operators to selector specific items from the Series，通过boolean运算过滤数据
'''
# Change False to True to see boolean indexing in action
if False:
    cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten'])
    print cuteness > 3
    print ""
    print cuteness[cuteness > 3]        # 过滤大于3的值
