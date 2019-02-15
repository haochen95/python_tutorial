# -*- coding: utf-8 -*-
import scrapy
from tecentJob.items import TecentjobItem

class TencentSpider(scrapy.Spider):

    name = 'tencent'
    allowed_domains = ['tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):

        for each in response.xpath("//tr[@class = 'even'] | //tr[@class = 'odd']"):
            # 初始化模型对象
            item = TecentjobItem()

            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        if self.offset < 100:
            self.offset += 10

        # 将请求重写发送给调度器入队列、出队列、交给下载器下载
        # 拼接新的rurl，并回调parse函数处理response
        # yield scrapy.Request(url， callback = self.parse)
		
		# 请求发出去之后，回来的响应由谁来处理
        # 如果没有响应文件就不会调用这个方法
        # 每处理完一页的数据之后，重新发送一页页面请求

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)