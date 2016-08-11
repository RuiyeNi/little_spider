import scrapy
import re
import os
import urllib

from carlingo.items import CarlingoItem

class carSpider(scrapy.Spider):
    name = "carlingo"
    allowed_domains = ["craigslist.org"]
    start_urls = [
        # just include one page in the current crawler
        "https://chicago.craigslist.org/sox/cto/5713391812.html",
    ]

    def parse(self, response):
        # initialize item
        item = CarlingoItem()
        sel = response.xpath('//span[@class="screen-reader-text"]')
        item['title'] = sel.xpath('//span[@id="titletextonly"]/text()').extract_first()
        item['location'] = sel.xpath('//small/text()').extract_first()
        item['price'] = sel.xpath('//span[@class="price"]/text()').extract_first()
            
        main = response.xpath('//section[@class = "userbody"]')
        item['post'] = main.xpath('//section[contains(@id,"postingbody")]/text()').extract()
        item['notice'] = main.xpath('//ul[@class="notices"]//li/text()').extract()
        item['time'] = main.xpath('//time[@class="timeago"]/@datetime').extract()
        pwd = os.getcwd()+'/'

        # tmp var cnt for matching multiple key value pairs in span
        cnt = 0
        for attr in response.xpath('//div[@class="mapAndAttrs"]//p[@class="attrgroup"]//span'):
            if not attr.xpath("text()").extract():
                item['model']=attr.xpath("//b/text()").extract_first() 
            else:
                tmp = attr.xpath("text()").extract()
                key = re.sub(' ','_',re.sub(':','',tmp[0]).strip())
                item[key] = attr.xpath("//b/text()").extract()[cnt] 
            cnt += 1
        
        # download images
        # first_img = response.xpath('//div[@class ="swipe-wrap"]//div//img/@src').extract()
        item['image_urls'] = [img.decode('utf-8').encode("ascii","ignore") for img in response.xpath('//img/@src').extract()]
        cnt = 1
        for img in item['image_urls']:
            urllib.urlretrieve(img,pwd+"crawlImages/"+str(cnt)+".jpg")
            cnt += 1
        yield item
        #     