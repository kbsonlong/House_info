# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from elasticsearch_dsl import Text, Date, Keyword, Integer, Document, Completion
from elasticsearch_dsl.connections import connections

# 新建连接
connections.create_connection(hosts="40.73.69.2")

class HouseType(Document):
    city_name= Text(analyzer="ik_max_word")
    district_name= Text(analyzer="ik_max_word")
    bizcircle_name= Text(analyzer="ik_max_word")
    address= Text(analyzer="ik_max_word")
    url = Keyword()
    open_date = Date()
    sale_status= Text(analyzer="ik_max_word")
    price = Integer()
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
        house.sale_status = item['sale_status']
        house.house_from = item['house_from']
        house.save()
        return item
