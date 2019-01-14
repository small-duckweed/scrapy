# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 类似django orm中的models.py
    # itme不管什么字段都是scrapy.Field() , 不区分int str等类型
    # 这是送给管道文件前的一个简单封装
    name = scrapy.Field()
