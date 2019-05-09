# -*- coding: utf-8 -*-
# @Time    : 2019-05-10 2:47
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : ajk.py
# @Software: PyCharm

import scrapy
import json
import re
import requests
import time
from bs4 import BeautifulSoup
from bk.items import BkItem




class AjkSpider(scrapy.Spider):
    name = 'ajk'
    allowed_domains = ['fang.anjuke.com']
    start_urls = ['https://gz.fang.anjuke.com/',
                  ]

    def isVaildDate(self, date):
        try:
            if ":" in date:
                time.strptime(date, "%Y-%m-%d %H:%M:%S")
            else:
                time.strptime(date, "%Y-%m-%d")
            return True
        except:
            return False
    def start_requests(self):
        for base_url in self.start_urls:
            for i in range(1,3):
                if i ==1:
                    url = '{}/loupan/all/'.format(base_url.strip('/'))
                else:
                    url = '{}/loupan/all/p{}/'.format(base_url.strip('/'),i)
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        content = soup.find_all('a',class_="lp-name")  # 返回每个楼盘的对应数据
        for house in content:
            # print(house)
            code = house["href"].split("/")[-1][:6]
            # print(code)
            real_href = "http://gz.fang.anjuke.com/loupan/canshu-{}.html?from=loupan_tab".format(code)  # 拼凑出楼盘详情页的url
            yield scrapy.Request(url=real_href,callback=self.real_parse)
    def real_parse(self,response):
        soup = BeautifulSoup(response.text, "lxml")
        a = re.findall(r'<div class="name">(.*?)</div>', str(soup))
        b = soup.find_all(class_="des")
        data = {}
        for (i, j) in zip(range(len(b)), a):
            data[j] = b[i].text.strip().strip("\t")
            data["url"] = response.url
        print(data)
        yield data

        item = BkItem()
        # for house in content:
        #     city_id = house['city_id']
        #     city_name = house['city_name']
        #     district_name = house['district_name']
        #     bizcircle_name = house['bizcircle_name']
        #     resblock_frame_area_range = house['resblock_frame_area_range']
        #     decoration = house['decoration']
        #     longitude = house['longitude']
        #     latitude = house['latitude']
        #     converged_rooms = house['converged_rooms']   ##户型
        #     resblock_name = house['resblock_name']
        #     frame_rooms_desc = house['frame_rooms_desc']
        #     address = house['address']
        #     house_type = house['house_type']
        #     sale_status = house['sale_status']
        #     open_date = house['open_date']
        #
        #
        #     if house['show_price'] != 0:
        #         price = house['show_price']
        #     elif house['reference_avg_price'] != 0:
        #         price = house['reference_avg_price']
        #     else:
        #         price = house['avg_price_start']
        #
        #     pant = "https(.*)fang.(.*).com(.*)"
        #     res = re.search(pant, response.url)
        #     house_from = res.group(2)
        #     url = 'https{}fang.{}.com{}'.format(res.group(1),res.group(2),house['url'])
        #     item['city_id'] = city_id
        #     item['city_name'] = city_name
        #     item['district_name'] = district_name
        #     item['bizcircle_name'] = bizcircle_name
        #     item['resblock_frame_area_range'] = resblock_frame_area_range
        #     item['decoration'] = decoration
        #     item['longitude'] = longitude
        #     item['latitude'] = latitude
        #     item['converged_rooms'] = converged_rooms
        #     item['resblock_name'] = resblock_name
        #     item['frame_rooms_desc'] = frame_rooms_desc
        #     item['address'] = address
        #     item['house_type'] = house_type
        #     item['sale_status'] = sale_status
        #     if self.isVaildDate(open_date):
        #         item['open_date'] = open_date
        #     else:
        #         item['open_date'] = '{}-{}-01'.format(open_date.split('-')[0],open_date.split('-')[1])
        #     item['price'] = price
        #     item['url'] = url
        #     item['house_from'] = house_from
        #     print(url)
        #     yield  item
