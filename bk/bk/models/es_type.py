# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 20:59
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : es_type.py
# @Software: PyCharm


# -*- coding:utf-8 -*-

from elasticsearch_dsl import Text, Date, Keyword, Integer, Document, Completion
from elasticsearch_dsl.connections import connections

# 新建连接
connections.create_connection(hosts="192.168.99.163")

class HouseType(Document):
    # city_name = Text(analyzer="ik_max_word")      #城市
    # district_name = Text(analyzer="ik_max_word")  #区域
    # bizcircle_name = Text(analyzer="ik_max_word") #
    # address = Text(analyzer="ik_max_word")        #地址
    #
    # url = Keyword()
    # # converged_rooms = Completion()                   #户型
    # price = Integer()                             #价格
    # open_date =Keyword()                         #开盘
    class Index:
        name = 'house_bk'

if __name__ == '__main__':
    HouseType.init()

