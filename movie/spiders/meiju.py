# -*- coding: utf-8 -*-
import scrapy
# from movie.movie.items import MovieItem
from ..items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'  # 爬虫名。一个项目下可能有多个爬虫，并且每个爬虫优先级、并发等设置。scrapy crawl [spider_name]
    allowed_domains = ['meijutt.com']   # 为了防止爬虫项目自动爬取到其它网站，设置限制，每一次请求前都会检查请求的网址是否属于这个域名下，是的话才允许请求。注意：爬取日志爬取网址后响应总为None，检查allowed_domain书写是否正确。值是一级域名。
    start_urls = ['https://www.meijutt.com/new100.html']  # 第一个请求的url，所有请求的入口。得到的response返回给 self.parse(self,response=response)

    def parse(self, response):
        # print(response.status_code, response.content, response.text)
        # 非框架下写法 dom = lxml.etree.HTML(response.text) ;  dom.xpath()

        # scrapy框架下正规写法 Selector(response.text).xpath('').extract()
        # 获取剧集名
        movie_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')  # [<li>对象, <li>对象, ...]
        for movie in movie_list:
            # . 是xpath的语法，表示在子标签(movie)基础上继续解析
            # name = movie.xpath('./h5/a/text()').extract()[0]  # xpath() 返回 [Selector()]
            # xpath().extract() 返回的是一个列表,提取出字符串  如: ['剧集名1']

            # xpath().extract_first() 返回结果集的第一项  如：'剧集名1'
            name = movie.xpath('./h5/a/text()').extract_first()
            # print(movie, name)  # 建议debug而不是print，不然因为并发会重复打印多次信息

            item = MovieItem()
            item["name"] = name  # 框架自己的语法，不用类对象的写法
            yield item   # 相当于同步脚本方法中的return