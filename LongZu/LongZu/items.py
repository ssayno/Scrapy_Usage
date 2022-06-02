# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LongzuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

    def __str__(self):
        return ""


'''

import scrapy
from ..items import LongzuItem


class DragonSpider(scrapy.Spider):
    def __init__(self):
        self.base_url = 'https://www.qu-la.com'
        self.count = 0
        self.iter_operator = iter(
            ['406593598116.html', '406593266116.html', '406592723116.html', '406592227116.html', '406592343116.html']
        )

    name = "dragon"

    def start_requests(self):
        start_urls = [
            'https://www.qu-la.com/booktxt/92162680116/406594275116.html',
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.count += 1
        content = response.css('div#txt::text').getall()
        context = "\par\n".join([segment.replace('\u3000', "") for segment in content])
        title = response.css('h1.chaptername::text').get()
        item = LongzuItem()
        item["title"] = title
        item["content"] = context
        yield item
        next_section = response.css('a#pb_next::attr(href)').get()
        if next_section is not None:
            yield scrapy.Request(url=self.base_url + next_section, callback=self.parse)
        else:
            try:
                yield scrapy.Request(url=self.base_url + next(self.iter_operator), callback=self.parse)
            except StopIteration as e:
                print("This book is finished")

'''
