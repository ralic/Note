# coding=utf-8
import pandas as pd
import numpy as np
import os

"""
Write a function named 'pollutantmean' that calculates the mean of a pollutant (sulfate or nitrate)
across a specified list of monitors. The function 'pollutantmean' takes three arguments:
 'directory', 'pollutant', and 'id'.
 Given a vector monitor ID numbers,
  'pollutantmean' reads that monitors'
  particulate matter data from the directory specified in the
   'directory' argument and returns the mean of the pollutant
   across all of the monitors, ignoring any missing values
   coded as NA. A prototype of the function is as follows
"""


def pollutantmena(directory, pollutant, monitor_start_id=1, monitor_end_id=332):
    assert pollutant == 'sulfate' or pollutant == 'nitrate', "this pollutant not exist!"
    # 保证初始id和结束id在[1, 332]之间
    monitor_start_id = 1 if monitor_start_id <= 0 else monitor_start_id
    monitor_end_id = monitor_start_id if monitor_end_id <= monitor_start_id \
        else (monitor_end_id if monitor_end_id < 332 else 332)
    print monitor_start_id, monitor_end_id
    # 'directory' is a character vector of length 1 indicating
    # the location of the CSV files
    # 'pollutant' is a character vector of length 1 indicating
    # the name of the pollutant for which we will calculate the
    # mean; either "sulfate" or "nitrate".
    elements = []

    # 读取对应id监测点的污染物
    for i in range(monitor_start_id, monitor_end_id + 1):
        if i < 10:
            filename = '00' + str(i) + '.csv'
        elif 10 <= i < 100:
            filename = '0' + str(i) + '.csv'
        else:
            filename = str(i) + '.csv'
        filename = os.path.join(directory, filename)
        df = pd.read_csv(filename)
        # 过滤出非NA的相应pollutant的数据（过滤某列）
        serise = df.loc[:, pollutant]
        array = serise[serise.notnull()].values
        elements.append(array)
    # 返回所有监测点列表对应污染物的平均值(排除NA值后)
    return round(np.mean(np.hstack(elements)), 3)


if __name__ == '__main__':
    print pollutantmena(r'C:\Users\admin\Downloads\rprog-data-specdata\specdata', 'nitrate', 70, 72)


