import scrapy
from ..items import JdItem


class JDSpider(scrapy.Spider):
    name = "JD"

    def __init__(self):
        self.page = 86

    def start_requests(self):
        urls = [
            f'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E5%8D%8E%E4%B8'
            f'%BAshou&pvid=a4336d2bdc7447d49ca8d82dd09258e7&page={page}' for page in range(0, self.page)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.css('div.gl-i-wrap')
        for product in products:
            item = JdItem()
            item["price"] = product.css('div:nth-child(3)>strong>i::text').get()
            phone_info = product.css('div:nth-child(4)>a>em::text').getall()
            name = "".join(phone_info).replace("】 ", "]").replace("【", "[").replace("/", "").strip()
            item["name"] = name
            item["manufacturer"] = product.css('div:nth-child(7)>span>a::attr(title)').extract_first()
            yield item

if __name__ == '__main__':
