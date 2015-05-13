# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取薪水和球队文档，并显示前五行
salaries = pd.read_csv(r"C:\Users\admin\Downloads\lahman-csv_2014-02-14\Salaries.csv")
teams = pd.read_csv(r"C:\Users\admin\Downloads\lahman-csv_2014-02-14\Teams.csv")
# print salaries.head()
# print teams.head()

# summary每个队伍每年的总薪水，形成一个新的DataFrame，然后显示前五行
newdf = salaries.groupby(['teamID', "yearID"]).sum()
# print newdf.head(5)
print pd.merge(newdf, teams, on='teamID')
