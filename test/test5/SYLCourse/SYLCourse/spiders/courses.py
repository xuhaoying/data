# -*- coding: utf-8 -*-
import scrapy
from ..items import ShiyanloucourseItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['shiyanlou.com']
    start_urls = ['https://www.shiyanlou.com/courses/?fee=free']


    def parse(self, response):
        # 解析当前页面各课程所在的 div, 将返回全部课程 Selector 列表
        courses = response.xpath('//div[@class="col-md-3 col-sm-6  course"]')
        # 遍历每个课程, 解析名称, 描述, 图片
        for course in courses:
            # 按定义好的 Item 结构返回数据
            item = ShiyanloucourseItem()
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract_first()
            item['description'] = course.xpath('.//div[@class="course-desc"]/text()').extract_first()
            item['image'] = course.xpath('.//div[@class="course-img"]/img/@src').extract_first()

            yield item

