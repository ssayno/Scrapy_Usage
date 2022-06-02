import scrapy


class OwnSpider(scrapy.Spider):
    name = "Own"

    start_urls = [
        'http://httpbin.org/get'
    ]

    def parse(self, response, **kwargs):
        file = open("./Learn/settings.py", "a+")
        name = "龙1"
        file.write(f"FILE_NAME=\"{name}\"")
        file.close()
        self.logger.debug(response.text)
