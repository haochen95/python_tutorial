# -*- coding: utf-8 -*-
import scrapy
# 导入链接规则匹配类，用来提取符合规则的链接
from scrapy.linkextractors import LinkExtractor
# 导入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider, Rule
from tencentCrawlSpider.items import TencentcrawlspiderItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    # 设置爬虫的允许范围
    allowed_domains = ['hr.tencent.com']
    # 第一次执行的时候这里发请求
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    # Reponse里链接的提取规则，返回符合匹配规则的链接匹配对象的列表
    pagelink = LinkExtractor(allow=("start=\d+"))
    # newLink = LinkExtractor(allow = ("12345"))

    # Rules的作用： 符合规则发送请求，并调用回调函数
    rules = [
        # 获取这个列表的链接，挨个发送请求，并且继续跟进，并调用指定的回调函数
        # 请求-》调度器-》入队列-》出队列-》下载器-》Response-》调用回调函数-》再次匹配LinkExtractor规则

        # 比如第一页： link = [0,1,2,3,4,1680]
        # 比如第二页： link = [0,2,3,4,5,1680]
        # 此时通过指纹判定是否请求已经发过？---》如何是的话，直接忽略
        Rule(pagelink, callback='parseTencent', follow=True)
        # Rule(newLink,callback="positionParse",follow=False)
    ]

    # 指定回调函数来处理响应-》给管道文件处理
    def parseTencent(self, response):
        for each in response.xpath("//tr[@class = 'even'] | //tr[@class = 'odd']"):
            # 初始化模型对象
            item = TencentcrawlspiderItem()

            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
