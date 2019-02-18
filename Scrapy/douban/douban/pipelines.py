# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

class DoubanPipeline(object):

    def __init__(self):
        host = settings["MONGDB_HOST"]
        port = settings["MONGDB_PORT"]
        dbname = settings["MONGDB_DBNAME"]
        sheetname = settings["MONGDB_SHEETNAME"]

        # 创建MongDB数据库连接
        client = pymongo.MongoClient(host=host, port=port)

        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库名字
        self.post = mydb[sheetname]

    def process_item(self, item, spider):

        data = dict(item)
        self.post.insert(data)

        return item
