# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field


class JdItem(Item):
    # define the fields for your item here like:
    name = Field()
    price = Field()
    manufacturer = Field()
