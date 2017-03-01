from scrapy.spiders import BaseSpider
import scrapy
from TestScraper.items import TestscraperItem

class MySpider(BaseSpider):
    name="testSpider"
    allowed_domains = [""] # put your domain here
    start_urls = [""] # put your url here

    def parse(self, response):

        items =[]
        for listElement in response.xpath('//div[@id="js__search-list"]/ul/li'):
            column1 = listElement.xpath('a/span[@class="search-list__column search-list__column--info-1"]')
            column2 = listElement.xpath('a/span[@class="search-list__column search-list__column--info-2"]')

            if len(column1.xpath('span').extract()) == 3 and len(column2.xpath('span').extract()) == 3:
                #print("******************************")
                address = column1.xpath('span/text()')[0].extract().strip(' \t\n\r')
                column1Row2 = column1.xpath('span/text()')[1].extract().split(",")
                column1Row3 = column1.xpath('span/text()')[2].extract().split(",")

                price = column2Row1 = column2.xpath('span/text()')[0].extract().strip(' \t\n\r')
                pricePerSquareMeter = column2Row2 = column2.xpath('span/text()')[1].extract().strip(' \t\n\r')
                date = column2Row3 = column2.xpath('span/text()')[2].extract().strip(' \t\n\r')

                if len(column1Row2) == 3 and len(column1Row3) == 2:
                    numberOfRooms = column1Row2[0].strip(' \t\n\r')
                    size = column1Row2[1].strip(' \t\n\r')
                    floor = column1Row2[2].strip(' \t\n\r')
                    type = column1Row3[0].strip(' \t\n\r')
                    location = column1Row3[1].strip(' \t\n\r')
                    #print ('{0:30} {1:10} {2:10} {3:10} {4:10} {5:10} {6:20} {7:20} {8:20}'.format(address, numberOfRooms, size, floor, type, location, price, pricePerSquareMeter, date))
                    item = TestscraperItem()
                    item['address'] = address
                    item['numberOfRooms'] = numberOfRooms
                    item['size'] = size
                    item['floor'] = floor
                    item['type'] = type
                    item['location'] = location
                    item['price'] = price
                    item['pricePerSquareMeter'] = pricePerSquareMeter
                    item['date'] = date
                    yield item;

        next_page = response.xpath('//a[@class="search-list__pagination-link search-list__pagination-link--next"]//@href').extract_first()
        #print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
