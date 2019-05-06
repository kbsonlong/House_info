# -*- coding: utf-8 -*-
import scrapy
import json

class BeikwSpider(scrapy.Spider):
    name = 'beikw'
    allowed_domains = ['fang.ke.com']
    start_urls = ['https://gz.fang.ke.com/']

    def start_requests(self):
        base_url = 'https://gz.fang.ke.com/loupan/pg'
        for i in range(1,10):
            url = '{}{}/?_t=1'.format(base_url,i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        house_lists = json.loads(response.body)['data']['list']
        for house in house_lists:
            city_id = house['city_id']
            city_name = house['city_name']
            district_name = house['district_name']
            bizcircle_name = house['bizcircle_name']
            resblock_frame_area_range = house['resblock_frame_area_range']
            decoration = house['decoration']
            longitude = house['longitude']
            latitude = house['latitude']
            converged_rooms = house['converged_rooms']   ##户型
            resblock_name = house['resblock_name']
            frame_rooms_desc = house['frame_rooms_desc']
            address = house['address']
            house_type = house['house_type']
            sale_status = house['sale_status']
            open_date = house['open_date']
            if house['show_price'] != 0 :
                price = house['show_price']

            elif house['reference_avg_price'] != 0:
                price = house['reference_avg_price']
            else:
                price = house['avg_price_start']
            url = self.start_urls[0]+house['url']