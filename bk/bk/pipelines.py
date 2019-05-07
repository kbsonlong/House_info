# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from elasticsearch_dsl import Text, Date, Keyword, Integer, Document, Completion
from elasticsearch_dsl.connections import connections

# 新建连接
connections.create_connection(hosts="192.168.99.163")

class HouseType(Document):
    class Index:
        name = 'house_bk'

class BkPipeline(object):
    def process_item(self, item, spider):
        return item


class ElasticsearchPipeline(object):
    def process_item(self,item,spider):
        house = HouseType()
        house.city_name = item['city_name']
        house.district_name = item['district_name']
        house.bizcircle_name = item['bizcircle_name']
        house.address = item['address']
        house.url = item['url']
        house.converged_rooms = item['converged_rooms']
        house.price = item['price']
        house.open_date = item['open_date']
        house.save()
        return item
