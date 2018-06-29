# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings


class SinaSpiderSpider(scrapy.Spider):
    name = 'sina_spider'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.cn/u/2778292197?filter=0&page=1']

    def start_requests(self):
        base_url = 'https://weibo.cn/u/2778292197?filter=0&page={}'
        for i in range(1,2):
            url = base_url.format(i)
            print('url: ', url)

            yield scrapy.Request(url=url, cookies=settings['COOKIES'])

    def parse(self, response):
        print('-------------------------')
        # print(response.body)
        div_list = response.xpath("//div[@class='c']//span[@class='ctt']/a/text()").extract()
        # print('topic: ', topic)
        # print('topic_len: ', len(topic))
        for i in range(1, len(div_list)-2):
            print('div_list', div_list)
            # topic = div_list[i].xpath("/div/span[@class='ctt']")
            # print('topic:', topic)