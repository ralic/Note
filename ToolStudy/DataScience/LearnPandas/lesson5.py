import pandas
import sys

d = {'one': [1, 1], 'two': [2, 2]}
i = ['a', 'b']
df = pandas.DataFrame(data=d, index=i)
print df
print df.index
stack = df.stack()
print stack, type(stack)
print stack.index
unstack = df.unstack()
print unstack