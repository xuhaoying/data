# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RepoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    repo_name = scrapy.Field()  # 仓库名称
    update_time = scrapy.Field()  # 仓库更新时间

    
