import scrapy
from ..items import LItem
import fileinput
import re


class LSpider(scrapy.Spider):
    name = "finally"

    start_urls = [
        'https://www.qu-la.com/booktxt/92162680116/406594275116.html',
    ]

    def __init__(self):
        self.base_url = 'https://www.qu-la.com'
        with open("./L/settings.py", "a+") as f:
            f.write("\nFILE_NAME=\"DRAGON\"")
        self.file_name = "DRAGON"
        self.chapter_name = iter([
            "哀悼之翼",
            "悼亡者之瞳",
            "黑月之潮-上",
            "黑月之潮-中",
            "黑月之潮-下",
            "奥丁之渊",
            "悼亡者之瞳"
        ])
        self.iter_operator = iter([
            'https://www.shizongzui.cc/longzu2aidaozhiyi/345.html',
            'https://www.qu-la.com/booktxt/76011220116/406593598116.html',
            'https://www.qu-la.com/booktxt/18022571116/406593266116.html',
            'https://www.qu-la.com/booktxt/46023530116/406592723116.html',
            'https://www.qu-la.com/booktxt/93753564116/406592227116.html',
            'https://www.qu-la.com/booktxt/85257252116/406592343116.html',
            'https://www.luoxiabook.com/longzu5/410040.html'
        ]
        )

    def parse(self, response, **kwargs):
        content = response.css('div#txt::text').getall()
        if content == []:
            content = response.css('div#BookText::text').getall()
            if content == []:
                content = response.css('div#content::text').getall()
        context = "\par\n".join([re.sub('^\u3000+', "", segment) for segment in content])
        title = response.css('h1.chaptername::text').get()
        if title is None:
            title = response.css('body > div > div > div > div > div.panel-footer.col-md-12 > h1::text').get()
        item = LItem()
        item["title"] = title
        item["content"] = context
        yield item
        next_section = response.css('a#pb_next::attr(href)').get()
        if next_section is None:
            next_section = response.css('body > div:nth-child(7) > div > h2 > a:nth-child(3)::attr(href)').get()
            if next_section is None:
                next_section = response.css(
                    'body > div > div > div > div > div.m-page > a.btn.btn-danger.pull-right.col-md-2.col-xs-3.col-sm-3::attr(href)').get()
        if next_section.endswith(".html") and next_section != response.url:
            if next_section.startswith("https:"):
                next_url = next_section
            else:
                next_url = self.base_url + next_section
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            try:
                self.add_the_chapter_name()
                print("添加成功")
                yield scrapy.Request(url=next(self.iter_operator), callback=self.parse)
            except StopIteration as e:
                print(e)
                print("This book is finished")

    def add_the_chapter_name(self):
        with open(f"./Content/{self.file_name}.tex", "a+") as f:
            f.write(f"\n\chapter{{{next(self.chapter_name)}}}\n")

        # file = fileinput.input("./L/settings.py", encoding="utf8", inplace=True)
        # for line in file:
        #     if line.find("FILE_NAME=") != -1:
        #         temp = line.split("=")[1]
        #         line = re.sub(temp, "\"" + next(self.file_name) + "\"", line)
        #     print('{}'.format(line), end='')
        # file.close()
