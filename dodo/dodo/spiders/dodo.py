"""main file for spider"""

from typing import Iterable

import requests
import scrapy
from scrapy import Request
from scrapy.http.request import VerboseCookie

from ..config import MY_USER_AGENT
from ..logger import LOGER


class DodoSpider(scrapy.Spider):
    """spider"""
    name = "Dodo"
    allowed_domains = ["dodopizza.ru"]
    start_urls = ["https://dodopizza.ru/sarapul"]

    def start_requests(self) -> Iterable[Request]:
        """hack block"""
        session_block = requests.session()
        hack_block = session_block.get(
            "https://dodopizza.ru/api/v1/stories/sdkkey",
            headers={"User-Agent": MY_USER_AGENT})
        for url in self.start_urls:
            yield Request(
                url=url,
                headers={"Authorization": f"Bearer {hack_block.content.decode()[2:-2]}"},
                cookies=[VerboseCookie(
                    name=cookie.name,
                    value=cookie.value,
                    domain=cookie.domain,
                    path=cookie.path,
                    secure=cookie.secure
                ) for cookie in session_block.cookies]
            )
        session_block.close()

    @LOGER.catch
    def parse(self, response):
        """getting data items"""
        sections = response.xpath(
            "//div[@id='react-app']/main/section[@class='sc-1tj5y7k-2 hLTpDK']"
        )
        for section in sections:
            articles = section.xpath(".//article")
            for article in articles:
                try:
                    yield {
                        "id": article.xpath("./@data-testid").get().split("_")[-1],
                        "name": article.xpath(".//div/a/span/text()").get(),
                        "description": article.xpath(".//div/text()").get().replace("\n", ""),
                        "section": section.xpath(".//h2/text()").get(),
                        "size": [25, 30, 35] if section.xpath(
                            ".//h2/text()"
                        ).get() == "Пиццы" else None,
                        "price": int(
                            "".join(char for char in article.xpath(
                                ".//footer/div/text()"
                            ).get() if char.isdigit())),
                        "images": [image.split(' ')[0] for image in
                                   article.xpath(".//picture/source/@data-srcset").getall()],
                    }
                except AttributeError:
                    LOGER.error({
                        "url": response.url,
                        "item_name": article.xpath(".//div/a/span/text()").get(),
                        "error": "description replace"
                    })
                    continue
                except TypeError:
                    LOGER.error({
                        "url": response.url,
                        "item_name": article.xpath(".//div/a/span/text()").get(),
                        "error": "getting price error"
                    })
