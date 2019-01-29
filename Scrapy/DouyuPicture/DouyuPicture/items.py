# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyupictureItem(scrapy.Item):
    # define the fields for your item here like:
    nickname = scrapy.Field()
    # 图片
    imagelink = scrapy.Field()
    # 图片位置
    imagePath = scrapy.Field()
