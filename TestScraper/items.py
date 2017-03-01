# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestscraperItem(scrapy.Item):
    date = scrapy.Field()
    address = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field()
    pricePerSquareMeter = scrapy.Field()
    numberOfRooms = scrapy.Field()
    floor = scrapy.Field()
    type = scrapy.Field()
    location = scrapy.Field()

