import scrapy


class DodoSpider(scrapy.Spider):
    name = "Dodo"
    allowed_domains = ["dodopizza.ru"]
    start_urls = ["https://dodopizza.ru"]

    def parse(self, response):
        pass
