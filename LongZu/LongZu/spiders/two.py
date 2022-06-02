import scrapy
import re
from ..items import LongzuItem


class TwoSpider(scrapy.Spider):
    name = "two"

    start_urls = [
        'https://www.shizongzui.cc/longzu2aidaozhiyi/345.html'
    ]

    def parse(self, response, **kwargs):
        content = response.css('div#BookText::text').getall()[1:]
        context = "\par\n".join([re.sub('^\u3000+', "", segment) for segment in content])
        item = LongzuItem()
        item["title"] = ""
        item["content"] = context
        yield item
        next_section = response.css('body > div:nth-child(7) > div > h2 > a:nth-child(3)::attr(href)').get()
        if next_section:
            yield scrapy.Request(url=next_section, callback=self.parse)
