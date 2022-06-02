# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy.exceptions
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import requests
from bs4 import BeautifulSoup


class WallpaperPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        images_path = [element['path'] for status, element in results if status]
        if not images_path:
            raise scrapy.exceptions.DropItem("Image Download Failed")
        return item

    def get_media_requests(self, item, info):
        image_url = item["images_url"]
        yield scrapy.Request(image_url)
