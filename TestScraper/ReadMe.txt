To export to csv:
scrapy crawl testSpider -o data.csv -t csv

To export to command window:
scrapy crawl testSpider

To laborate with scrapy (result is stored in response variable):
scrapy shell https://www.com
Example:
response.xpath('//a[class="search-list__pagination-link search-list__pagination-link--next"]/@href').extract_first()

External python libraries:
python 3.5 win32: https://www.python.org/downloads/windows/
pywin32: pywin32-220.win32-py3.5.exe https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/
scrapy

