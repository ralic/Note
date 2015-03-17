# coding=utf-8
import pandas
import pandasql
"""
csv文件读写demo
pandas.read_csv()
pandas.DataFrame.to_csv()
"""

def add_full_name(path_to_csv, path_to_new_csv):
    # Assume you will be reading in a csv file with the same columns that the
    # Lahman baseball data set has -- most importantly, there are columns
    # called 'nameFirst' and 'nameLast'.
    # 1) Write a function that reads a csv
    # located at "path_to_csv" into a pandas dataframe and adds a new column
    # called 'nameFull' with a player's full name.
    #
    # For example:
    #    for Hank Aaron, nameFull would be 'Hank Aaron',
    # 2)Write the data in the pandas dataFrame to a new csv file located at
    # path_to_new_csv

    df = pandas.read_csv(path_to_csv)
    df["nameFull"] = df["nameFirst"] + df["nameLast"]
    df.to_csv(path_to_new_csv)


def select_first_50(filename):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)

    # Select out the first 50 values for "registrar" and "enrolment_agency"
    # in the aadhaar_data table using SQL syntax.
    #
    # Note that "enrolment_agency" is spelled with one l. Also, the order
    # of the select does matter. Make sure you select registrar then enrolment agency
    # in your query.
    # 使用sql语句查询
    q = "select registrar, enrolment_agency from aadhaar_data limit 50"

    #Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution

if __name__ == "__main__":
    # For local use only
    # If you are running this on your own machine add the path to the
    # Lahman baseball csv and a path for the new csv.
    path_to_csv = "Master.csv"
    path_to_new_csv = "haha.csv"
    add_full_name(path_to_csv, path_to_new_csv)
