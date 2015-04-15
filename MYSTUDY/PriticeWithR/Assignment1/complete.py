# coding=utf-8
import pandas as pd
import numpy as np
import os


# 获得指定监测点所有没有
def complete(directory, lst):
    """
    complete("specdata", [2, 4, 8, 10, 12])
    ##   id nobs
    ## 1  2 1041
    ## 2  4  474
    ## 3  8  192
    ## 4 10  148
    ## 5 12   96
    """
    idlist = []
    nobslist = []
    for i in lst:
        idlist.append(i)
        if i < 10:
            filename = '00' + str(i) + '.csv'
        elif 10 <= i < 100:
            filename = '0' + str(i) + '.csv'
        else:
            filename = str(i) + '.csv'
        filename = os.path.join(directory, filename)
        df = pd.read_csv(filename)
        # 选取sulfate" or "nitrate"不为nan的行
        df = df[(df['sulfate'].notnull()) & (df['nitrate'].notnull())]
        # 计算行数
        nobslist.append(df.count()[0])
    # 使用zip构建数据框
    # 返回一个两列的数据框，行索引从1开始
    return pd.DataFrame(data=zip(idlist, nobslist), columns=['id', 'nobs'], index=range(1, len(idlist)+1))



if __name__ == '__main__':
    print complete(r'C:\Users\admin\Downloads\rprog-data-specdata\specdata', [2, 4, 8, 10, 12])