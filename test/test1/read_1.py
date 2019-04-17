import os
import pandas as pd

cur_path = os.getcwd()  # 当前路径

def convert(file):
    """
    读取 JSON 文件 file 的前 1000 行数据，
    并将这 1000 行数据储存为 HDF5 数据文件 user_study.h5
    """
    file_path = os.path.join(cur_path, file)  
    df = pd.read_json(file_path)
    df1 = df[:1000]
    h5_path = os.path.join(cur_path, "user_study.h5")
    df1.to_hdf(h5_path, key="df1", format="table")
    # print(pd.read_hdf('user_study.h5', key='df1'))


convert("users_data.json")