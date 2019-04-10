# -*- coding: utf-8 -*-
import scrapy
from pandatv.items import PandatvItem
import time

class PandaSpider(scrapy.Spider):
    name = 'panda'
    allowed_domains = ['panda.tv']
    start_urls = ['https://www.panda.tv/cate/lol']

    def parse(self, response):
        list = response.xpath("//div[@class='list-container']//li")
        for i_item in list:
            panda_item=PandatvItem()
            panda_item['name']=i_item.xpath(".//span[@class='video-nickname']/@title").extract()
            panda_item['number']=i_item.xpath(".//span[@class='video-number']/text()").extract()
            yield panda_item

