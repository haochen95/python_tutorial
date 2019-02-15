# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=30']

    rules = [
        Rule(LinkExtractor(allow=('type=4&page=\d+'))),
        Rule(LinkExtractor(allow = ('/html/question/\d+/\d+.shtml')), callback = 'parseDongguan')
    ]

    def parseDongguan(self, response):

        item = DongguanItem()

        item['title'] = response.xpath('//div[@class="wzy1"]/table[1]//tr/td[2]/span[1]/text()').extract()[0].split('：')[-1]
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr/td/text()').extract()[0]
        item['url'] = response.url
        item['number'] = response.xpath('//div[@class="wzy1"]/table[1]//tr/td[2]/span[2]/text()').extract()[0].split(':')[-1]

        yield item
