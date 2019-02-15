#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : start.py
# @Author   : Hao Chen
# @Date     : 2019/2/15 10:12
# @Contact  : haochen273@gmail.com

from scrapy import cmdline

cmdline.execute("scrapy crawl itcast".split())