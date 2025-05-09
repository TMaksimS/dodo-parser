"""broker"""
# pylint: disable = relative-beyond-top-level
import logging

from faststream.rabbit import RabbitBroker, RabbitQueue

from .schemas import DodoProductSchema
from ..config import RABBIT_URL, QUEUE_DODO

broker = RabbitBroker(RABBIT_URL, timeout=30, max_consumers=10, log_level=logging.INFO)

async def send_item_dodo_to_rabbit(create: DodoProductSchema):
    """Отправка обьекта в очередь"""
    async with broker as br:
        await br.publish(
            create,
            queue=QUEUE_DODO,
            timeout=30,
        )
    return True

async def create_queue(queue_name: str):
    """создание очереди"""
    async with broker:
        await broker.declare_queue(RabbitQueue(queue_name))
