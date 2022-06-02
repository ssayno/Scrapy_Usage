import scrapy
import re
from ..items import LongzuItem


class TwoSpider(scrapy.Spider):
    name = "five"

    start_urls = [
        'https://www.luoxiabook.com/longzu5/410040.html'
    ]

    def parse(self, response, **kwargs):
        content = response.css('div#content::text').getall()
        context = "\par\n".join([re.sub('^\n(\xa0)+', "", segment) for segment in content])
        item = LongzuItem()
        item["title"] = response.css('body > div > div > div > div > div.panel-footer.col-md-12 > h1::text').get()
        item["content"] = context
        yield item
        next_section = response.css('body > div > div > div > div > div.m-page > a.btn.btn-danger.pull-right.col-md-2.col-xs-3.col-sm-3::attr(href)').get()
        if next_section:
            yield scrapy.Request(url=next_section, callback=self.parse)
