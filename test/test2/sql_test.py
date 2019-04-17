import os
import sqlite3
import pandas as pd

def count(file, user_id):
    """
    查询指定用户 ID 学过课程的累计学习分钟数，并作为函数返回值(int类型)。
    如果指定用户 ID 不存在，则返回 0。

    file 用于连接指定名称的数据库文件
    user_id 用户 ID
    """
    sql_con = sqlite3.connect(file)
    sql_query = """SELECT SUM(minutes) FROM data 
                where user_id = {}
                """.format(user_id)
    df_minutes = pd.read_sql(sql_query, sql_con)
    # print(df_minutes)
    # print(type(df_minutes))
    # print(df_minutes['SUM(minutes)'][0])
    # print(type(df_minutes['SUM(minutes)'][0]))
    sum_minutes = df_minutes['SUM(minutes)'][0]
    try:
        sum_minutes = int(sum_minutes)
    except Exception as e:
        sum_minutes = 0
    sql_con.close()
    print(sum_minutes)
    return sum_minutes

count("users_data.sqlite", 8490)