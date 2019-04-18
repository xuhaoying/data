# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SylCourseItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 课程名称
    description = scrapy.Field()  # 课程介绍
    image = scrapy.Field()  # 课程图片

