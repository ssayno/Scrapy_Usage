import os

import scrapy
from First.LongZu.LongZu.items import LongzuItem
import re


class DragonSpider(scrapy.Spider):
    name = "dragon"

    def __init__(self):
        self.base_url = 'https://www.qu-la.com'
        self.count = 0
        self.iter_operator = iter(
            ['https://www.qu-la.com/booktxt/76011220116/406593598116.html',
             'https://www.qu-la.com/booktxt/18022571116/406593266116.html',
             'https://www.qu-la.com/booktxt/46023530116/406592723116.html',
             'https://www.qu-la.com/booktxt/93753564116/406592227116.html',
             'https://www.qu-la.com/booktxt/85257252116/406592343116.html']
        )
        self.file_name = iter([
            "龙1",
            "龙2",
            "龙3上",
            "龙3中",
            "龙3下",
            "龙4",
            "龙5"
        ])

    start_urls = [
        'https://www.qu-la.com/booktxt/92162680116/406594275116.html',
    ]

    def parse(self, response):
        self.count += 1
        content = response.css('div#txt::text').getall()
        context = "\par\n".join([segment.replace('\u3000', " ") for segment in content])
        title = response.css('h1.chaptername::text').get()
        item = LongzuItem()
        item["title"] = title
        item["content"] = context
        yield item
        next_section = response.css('a#pb_next::attr(href)').get()
        if next_section.endswith(".html"):
            yield scrapy.Request(url=self.base_url + next_section, callback=self.parse)
        else:
            try:
                self.change_the_file_name()
                yield scrapy.Request(url=next(self.iter_operator), callback=self.parse)
            except StopIteration as e:
                print("This book is finished")

    def change_the_file_name(self):
        file = open("./LongZu/settings.py", "w+", encoding="utf8")
        lines = file.readlines()
        need = lines[-1]
        if need.find("FILE_NAME=") == -1:
            file.write(f"FIlE_NAME={next(self.file_name)}")
        else:
            temp = need.split("=")[1]
            lines[-1].replace(temp, next(self.file_name))
        file.writelines(lines)
        file.close()
