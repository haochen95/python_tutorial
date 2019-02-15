# -*- coding: utf-8 -*-
import scrapy
from dongguanSpider.items import DongguanItem



class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0

    start_urls = [url + str(offset)]





    def parse(self, response):
        # 每一页的所有帖子的链接集合
        links = response.xpath('//div[@class="greyframe"]/table//td/a[@class="news14"]/@href').extract()
        # 迭代取出集合里的链接
        for link in links:
            # 提取列表里每个帖子的链接，发送请求并调用parse——item来处理
            yield scrapy.Request(link, callback=self.parse_item)

        # 页面终止条件成立前，会一直自增offset的值，并发送新的页面请求，调用parse方法处理
        if self.offset<=71160:
            self.offset +=30

            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


    def parse_item(self, response):

        item = DongguanItem()

        item['title'] = response.xpath('//div[@class="wzy1"]/table[1]//tr/td[2]/span[1]/text()').extract()[0].split('：')[-1]
        item['url'] = response.url
        item['number'] = response.xpath('//div[@class="wzy1"]/table[1]//tr/td[2]/span[2]/text()').extract()[0].split(':')[-1]

        # 是否是图片
        content_pic = response.xpath('//div[@class="textpic"]/img/@src').extract()

        if len(content_pic)==0:
            content_no_pic = response.xpath('//div[@class="wzy1"]/table[2]//tr/td/text()').extract()[0]
            item['content'] = "".join(content_no_pic).replace("\xa0", "")
        else:
            item['content'] = "".join(content_pic[0]).replace("\xa0", "")

        yield item