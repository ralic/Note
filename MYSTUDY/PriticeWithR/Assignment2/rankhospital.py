# coding=utf-8
import pandas as pd
import numpy as np


# 获得在某个状态下指定排名的医院名称（最好是指30内某种疾病死亡率升序排名）
def rankhospital(state, outcome, num):
    """
    :param state: 状态
    :param outcome: 疾病（“heart attack”, “heart failure”, or “pneumonia”）
    :param num: 表按最低死亡率排名排第num个数据， 其中best表示排第一，worst表示排最后
    """

    # Read outcome data
    out_date = pd.read_csv(r"C:\Users\admin\Downloads\rprog-data-ProgAssignment3-data\outcome-of-care-measures.csv")
    # Check that state and outcome are valid
    if outcome not in ["heart attack", "heart failure", "pneumonia"]:
        raise ValueError("invalid outcome")
    if state not in set(out_date['State'].values):
        raise ValueError("invalid state")
    if not isinstance(num, int) and num not in ["best", "worst"]:
        raise ValueError("invalid num")
    colnumber = 23 if outcome == "pneumonia" else (17 if outcome == "heart failure" else 11)
    # 获得指定列的名称
    colname = out_date.columns[colnumber - 1]
    # 过滤出指定状态下的有效数据
    out_date = out_date[(out_date["State"] == state) & (out_date[colname] != "Not Available")]
    # 提取子数据框，方便操作
    sub_dataframe = out_date.loc[:, ["Hospital Name", colname]]
    sub_dataframe[colname] = np.float32(sub_dataframe[colname])
    # 优先死亡率升序排列，然后按医院名排序
    sub_dataframe = sub_dataframe.sort([colname, "Hospital Name"])
    # 获得行数
    rows = len(sub_dataframe)
    result = sub_dataframe["Hospital Name"].values
    if num == "best":
        return result[0]
    elif num == "worst":
        return result[-1]
    else:
        if num <= rows:
            return result[num - 1]
        else:
            return "NA"

if __name__ == '__main__':
    print rankhospital("TX", "heart failure", 4)
    # print rankhospital("MN", "heart attack", 5000)
    # print rankhospital("MD", "heart attack", "worst")