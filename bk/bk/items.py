# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city_id = scrapy.Field()
    city_name = scrapy.Field()
    district_name = scrapy.Field()
    bizcircle_name = scrapy.Field()
    resblock_frame_area_range = scrapy.Field()
    decoration = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    converged_rooms = scrapy.Field()
    resblock_name = scrapy.Field()
    frame_rooms_desc = scrapy.Field()
    address = scrapy.Field()
    house_type = scrapy.Field()
    sale_status = scrapy.Field()
    open_date = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    house_from = scrapy.Field()

