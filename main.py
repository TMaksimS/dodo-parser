"""main file"""
# pylint: disable = [no-name-in-module, import-error, raise-missing-from, broad-exception-raised]
import asyncio
import json

from aiormq import AMQPConnectionError
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from dodo.dodo.config import MY_USER_AGENT, QUEUE_DODO
from dodo.dodo.rabbitmq.rabbit_broker import create_queue, send_item_dodo_to_rabbit, broker
from dodo.dodo.rabbitmq.schemas import DodoProductSchema
from dodo.dodo.spiders.dodo import DodoSpider


def start_scrapy():
    """мэйн функция для запуска скраппера"""
    settings = get_project_settings()
    settings.set("BOT_NAME", "dodo")
    settings.set("SPIDER_MODULES", ["dodo.dodo.spiders"])
    settings.set("NEWSPIDER_MODULE", "dodo.dodo.spiders")
    settings.set("USER_AGENT", MY_USER_AGENT)
    settings.set("ROBOTSTXT_OBEY", False)
    settings.set("ITEM_PIPELINES", {
       "dodo.dodo.pipelines.DodoPipeline": 800,
    })
    settings.set("TWISTED_REACTOR", "twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    settings.set("FEED_EXPORT_ENCODING", "utf-8")
    process = CrawlerProcess(settings)
    process.crawl(DodoSpider)
    process.start()

async def send_items_to_rabbit(file_path: str):
    """коронутина для отправки всех обьектов в брокера"""
    async with broker as br:
        with open(file_path) as file:
            for item in file.readlines():
                await br.publish(
                    DodoProductSchema(**json.loads(item)),
                    queue=QUEUE_DODO,
                    timeout=30,
                )

if __name__ == "__main__":
    try:
        asyncio.run(create_queue(QUEUE_DODO))
    except AMQPConnectionError:
        raise Exception("Error when connecting to rabbit")
    start_scrapy()
    asyncio.run(send_items_to_rabbit("dodospider.json"))