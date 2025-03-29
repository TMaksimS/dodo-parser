"""main file"""

import asyncio

from aiormq import AMQPConnectionError
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from dodo.dodo.config import MY_USER_AGENT, QUEUE_DODO
from dodo.dodo.rabbitmq.rabbit_broker import create_queue
from dodo.dodo.spiders.dodo import DodoSpider


def start_scrapy():
    settings = get_project_settings()
    settings.set("BOT_NAME", "dodo")
    settings.set("SPIDER_MODULES", ["dodo.dodo.spiders"])
    settings.set("NEWSPIDER_MODULE", "dodo.dodo.spiders")
    settings.set("USER_AGENT", MY_USER_AGENT)
    settings.set("ROBOTSTXT_OBEY", False)
    settings.set("ITEM_PIPELINES", {
       "dodo.dodo.pipelines.DodoPipeline": 300,
    })
    settings.set("TWISTED_REACTOR", "twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    settings.set("FEED_EXPORT_ENCODING", "utf-8")
    process = CrawlerProcess(settings)
    process.crawl(DodoSpider)
    process.start()

if __name__ == "__main__":
    try:
        asyncio.run(create_queue(QUEUE_DODO))
    except AMQPConnectionError:
        raise Exception("Error when connecting to rabbit")
    start_scrapy()

