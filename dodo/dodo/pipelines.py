"""pipeline for scrapy"""
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from .logger import LOGER
from .rabbitmq.rabbit_broker import send_item_dodo_to_rabbit
from .rabbitmq.schemas import DodoProduct


class DodoPipeline:
    # pylint: disable = too-few-public-methods
    """Default Pipeline object"""

    @LOGER.catch
    async def process_item(self, item, spider):
        # pylint: disable = unused-argument
        """default scrapy func with sender task"""
        await send_item_dodo_to_rabbit(DodoProduct(**item))
        return item
