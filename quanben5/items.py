# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import json
import scrapy
from scrapy import Field

class ArtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    table = 'art_art'
    a_title = Field()
    a_info = Field()
    a_content = Field()
    a_img = Field()
    a_tag_id = Field()

# class TagItem(scrapy.Item):
#     table = 'art_tag'
#     t_name = Field()
