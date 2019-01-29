# -*- coding: utf-8 -*-
import scrapy
import json
from DouyuPicture.items import DouyupictureItem


class DouyumeinvSpider(scrapy.Spider):
    name = 'douyumeinv'
    allowed_domains = ['capi.douyucdn.cn']

    init_url ='http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [init_url + str(offset)]

    def parse(self, response):
        data = json.loads(response.text)["data"]  # 将jason转换为python的列表

        for each in data:

            item = DouyupictureItem()
            item['nickname'] = each['nickname']
            item['imagelink'] = each['vertical_src']

            yield item

        if self.offset<=10:
            self.offset +=1

        yield scrapy.Request(self.init_url + str(self.offset), callback=self.parse)
