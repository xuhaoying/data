# -*- coding: utf-8 -*-

import pandas as pd

class ShiyanloucourseItem(object):
    # 爬虫工作时
    def process_item(self, item, spider):
        # 读取 item 数据
        name = item['name']
        description = item['description']
        image = item['image']
        # 每条数据组成临时 df_temp
        df_temp = pd.DataFrame([[name, description, image]], columns=['name', 'description', 'image'])
        # 将 df_temp 合并到 df
        self.df = self.df.append(df_temp, ignore_index=True)

        return item

    #当爬虫启动时
    def open_spider(self, spider):
        # 新建一个带列名的空白 df
        self.df = pd.DataFrame(columns=['name', 'description', 'image'])

    # 当爬虫关闭时
    def close_spider(self, spider):
        # 将 df 存储为 csv 文件
        pd.DataFrame.to_csv(self.df, "courses.csv")