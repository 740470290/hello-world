# -*- coding: utf-8 -*-
import scrapy
from pandatv.items import PandatvItem

class PandaSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyu.com']
    start_urls = ['https://www.douyu.com/g_LOL']

    def parse(self, response):
        list = response.xpath("//div[@id='live-list-content']/ul[@id='live-list-contentbox']/li")
        for i_item in list:
            panda_item=PandatvItem()
            panda_item['name']=i_item.xpath(".//span[@class='dy-name ellipsis fl']/text()").extract()
            panda_item['number']=i_item.xpath(".//span[@class='dy-num fr']/text()").extract()
            panda_item['title']=i_item.xpath("./a[@class='play-list-link']/@title").extract()
            yield panda_item
