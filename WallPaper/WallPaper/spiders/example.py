import scrapy
import requests
from bs4 import BeautifulSoup
from ..items import WallpaperItem


def deep_parse(response):
    images_url = response.css("#wallpaper::attr(src)").get()
    item = WallpaperItem()
    item["images_url"] = images_url
    yield item


class ExampleSpider(scrapy.Spider):
    name = 'wallpaper'

    start_urls = [
        'https://wallhaven.cc/'
    ]

    def parse(self, response):
        links = response.css('div.feat-row>span>a::attr(href)').getall()
        for link in links:
            yield scrapy.Request(url=link, callback=deep_parse)
