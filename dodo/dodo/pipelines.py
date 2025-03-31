"""pipeline for scrapy"""
# pylint: disable = [unspecified-encoding consider-using-with unused-argument attribute-defined-outside-init]
import json

from itemadapter import ItemAdapter


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class DodoPipeline:
    # pylint: disable = too-few-public-methods
    """Default Pipeline object"""

    def open_spider(self, spider):
        """действие при откритии паука"""
        self.file = open("dodospider.json", "w")

    def close_spider(self, spider):
        """дейтсвие при закрытии паука"""
        self.file.close()

    def process_item(self, item, spider):
        """обработка обьекта"""
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
