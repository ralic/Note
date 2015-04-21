# coding=utf-8
# 避免提取自数据库，共享引用,使用‘，’号提取
import numpy as np
import pandas as pd


def rankall(outcome, num):
    """
    :param outcome: 疾病（“heart attack”, “heart failure”, or “pneumonia”）
    :param num: 表按最低死亡率排名排第num个数据， 其中best表示排第一，worst表示排最后
    :return 返回一个数据框，[对应状态第num的医院名称, 某状态]
    """
    # Read outcome data
    out_date = pd.read_csv(r"C:\Users\admin\Downloads\rprog-data-ProgAssignment3-data\outcome-of-care-measures.csv")
    # Check that state and outcome are valid
    if outcome not in ["heart attack", "heart failure", "pneumonia"]:
        raise ValueError("invalid outcome")
    if not isinstance(num, int) and num not in ["best", "worst"]:
        raise ValueError("invalid num")
    colnumber = 23 if outcome == "pneumonia" else (17 if outcome == "heart failure" else 11)
    colname = out_date.columns[colnumber - 1]
    # 形成最终数据框的列表：医院名称列表，状态列表
    hospital_name = []
    statelist = []
    states = list(set(out_date['State']))
    for the_state in states:
        statelist.append(the_state)
        df = out_date[(out_date["State"] == the_state) & (out_date[colname] != "Not Available")]
        # 提取子数据框
        df = df.loc[:, ["Hospital Name", colname]]
        df.loc[:, colname] = np.float32(df[colname])
        # 优先死亡率升序排列，然后按医院名排序
        df = df.sort([colname, "Hospital Name"])
        rows = len(df)
        if rows == 0:
            # 空数据框自然填充NAN
            hospital_name.append(np.nan)
            continue
        hospitals = df["Hospital Name"].values
        if num == "best":
            hospital_name.append(hospitals[0])
        elif num == "worst":
            hospital_name.append(hospitals[-1])
        else:
            if num > rows:
                hospital_name.append(np.nan)
            else:
                hospital_name.append(hospitals[num - 1])
    result = pd.DataFrame(data=zip(hospital_name, statelist), columns=["hospital", "state"], index=statelist)
    # 返回数据框，按状态名称排序
    return result.sort(["state"])


if __name__ == '__main__':
    # print rankall("heart attack", 20).head(10)
    # print rankall("pneumonia", "worst").tail(3)
    print rankall("heart failure", "best").tail(10)