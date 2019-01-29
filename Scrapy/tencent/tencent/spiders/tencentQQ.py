# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentqqSpider(scrapy.Spider):
    name = 'tencentQQ'
    allowed_domains = ['tencent.com']
    init_url = 'https://hr.tencent.com/position.php?&start='
    offset = 0

    start_urls = [init_url + str(offset)]


    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = TencentItem()

            # 职位名
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]  # 返回字符串
            # 详情链接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        if self.offset < 100:
            self.offset += 10

        # 请求发出去之后，回来的响应由谁来处理
        # 如果没有响应文件就不会调用这个方法
        # 每处理完一页的数据之后，重新发送一页页面请求

        yield scrapy.Request(self.init_url + str(self.offset), callback=self.parse)