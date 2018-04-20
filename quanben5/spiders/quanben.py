# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request
from quanben5.items import *

class QuanbenSpider(scrapy.Spider):
    name = 'quanben'
    allowed_domains = ['quanben5.com']
    start_urls = ['http://www.quanben5.com/']
    dicTag = {
        '玄幻': 1,
        '都市': 2,
        '仙侠': 3,
        '武侠': 4,
        '言情': 5,
        '穿越': 6,
        '网游': 7,
        '奇幻': 8,
        '科幻': 9,
        '悬疑': 10,
        '青春': 11,
        '校园': 12,
        '军事': 13,
        '历史': 14,
        '同人': 15,
        '经典': 16,
        '畅销': 17,
        '其他': 18
    }

    def parse(self, response):
        # print(response.text)
        # 获取小说链接
        post_url = 'http://www.quanben5.com%s'
        post_list = response.xpath('//div[@class="nav"]//a/@href').extract()
        for post in post_list:
            url = post_url%post
            # print(url)
            request = Request(url,callback=self.parse_category)
            yield request


    def parse_category(self,response):
        # print(response.url)
        post_url = 'http://www.quanben5.com%s'
        try:
            post_list = response.xpath('//div[@class="pic_txt_list"]/h3/a/@href').extract()
            for post in post_list:
                url = post_url % post
                # print(url)
                request = Request(url, callback=self.parse_post)

                yield request
        except Exception as e:
            print(e)


    def parse_post(self,reponse):

        # print(reponse.text)
        post = ArtItem()
        post['a_title'] = reponse.xpath('//div[@class="pic_txt_list"]/h3/span/text()').get()
        author = reponse.xpath('//div[@class="pic_txt_list"]/p/text()').extract()[0]
        user = reponse.xpath('//div[@class="pic_txt_list"]/p/span/text()').extract()[0]
        info = author+user
        post['a_info'] = info
        post['a_img'] = reponse.xpath('//div[@class="pic"]/img/@src').get()
        post['a_content'] = reponse.xpath('//div[@class="description"]/p/text()').get()
        tag = reponse.xpath('//div[@class="pic_txt_list"]/p/span/text()').extract()[1]

        id = QuanbenSpider.dicTag[tag]
        post['a_tag_id'] = id
        # print(post)
        yield post

    # def part_tag(self):
    #     t_names =QuanbenSpider.dicTag.keys()
    #     post1 = TagItem()
    #
    #     for t_name in t_names:
    #         post1['t_name'] = t_name
    #     print(post1)
