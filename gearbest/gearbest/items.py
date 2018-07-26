# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GearbestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AppliancesItem(scrapy.Item):
    product_name = scrapy.Field()
    product_sale_price = scrapy.Field()
    product_origin_price = scrapy.Field()
    product_comment = scrapy.Field()
    product_url = scrapy.Field()
    product_pic_url = scrapy.Field()
    # product_like = scrapy.Field()
    product_favorite = scrapy.Field()
    product_rank = scrapy.Field()
    product_sale_amount = scrapy.Field()


