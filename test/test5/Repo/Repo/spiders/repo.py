# -*- coding: utf-8 -*-
import scrapy
from Repo.items import RepoItem

class RepoSpider(scrapy.Spider):
    name = 'repo'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        # 解析页面
        repos = response.xpath('//div[@class="col-9 d-inline-block"]')
        for repo in repos:
            item = RepoItem()
            item['repo_name'] = repo.xpath('.//a[@itemprop="name codeRepository"]/text()').extract_first()
            item['update_time'] = repo.xpath('.//relative-time/@datetime').extract_first()

            yield item
