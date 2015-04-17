# coding=utf-8
import pandas as pd
import numpy as np


# 获得在某个状态下最好的医院名称（最好是指30内某种疾病死亡率最低的医院）
def best(state, outcome):
    """
    :param state: 状态
    :param outcome: 疾病（“heart attack”, “heart failure”, or “pneumonia”）
    """

    # Read outcome data
    out_date = pd.read_csv(r"C:\Users\admin\Downloads\rprog-data-ProgAssignment3-data\outcome-of-care-measures.csv")
    # Check that state and outcome are valid
    if outcome not in ["heart attack", "heart failure", "pneumonia"]:
        raise ValueError("invalid outcome")
    if state not in set(out_date['State'].values):
        raise ValueError("invalid state")
    colnumber = 23 if outcome == "pneumonia" else (17 if outcome == "heart failure" else 11)
    # Return hospital name in that state with lowest 30-day death
    # 获得指定列的名称
    colname = out_date.columns[colnumber - 1]
    # 过滤出指定状态下的有效数据
    out_date = out_date[(out_date["State"] == state) & (out_date[colname] != "Not Available")]
    # 提取子数据框，方便操作
    sub_dataframe = out_date.loc[:, ["Hospital Name", colname]]
    # 将字符串数据转换成浮点型
    sub_dataframe[colname] = np.float32(sub_dataframe[colname])
    # 提取死亡率最小的数据
    sub_dataframe = sub_dataframe[sub_dataframe[colname] == sub_dataframe[colname].min()]
    # 按医院名称排序
    sub_dataframe = sub_dataframe.sort(['Hospital Name'])
    # 得到排名最前的医院（即死亡率最低）
    return sub_dataframe["Hospital Name"].values[0]


if __name__ == '__main__':
    print best("TX", "heart attack")
    print best("TX", "heart failure")
    print best("MD", "heart attack")
    print best("MD", "pneumonia")

