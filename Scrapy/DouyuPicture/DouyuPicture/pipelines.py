# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os

class DouyupicturePipeline(object):
    # 获取setting中设置的变量值
    IMAHE_STORE = get_project_settings().get("IMAGE_STORE")

    def get_media_requests(self, item, info):
        image_url = item['imagelink']
        # 这个方法会调用item_complete
        yield scrapy.Request(image_url)

    def item_completed(self,result,item,info):
        image_path = [x['path'] for ok,x in result if ok]

        os.rename(self.IMAHE_STORE + image_path[0], self.IMAHE_STORE + item['nickname'] + ".jpg")

        item['imagePath'] = self.IMAHE_STORE + item['nickname']
    #
    # def process_item(self, item, spider):
    #     return item