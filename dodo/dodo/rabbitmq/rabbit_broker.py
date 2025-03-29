"""broker"""
from faststream.rabbit import RabbitBroker, RabbitQueue

from .schemas import DodoProduct
from ..config import RABBIT_URL, QUEUE_DODO

broker = RabbitBroker(RABBIT_URL, timeout=15)

async def send_item_dodo_to_rabbit(create: DodoProduct):
    """Отправка обьекта в очередь"""
    async with broker:
        await broker.publish(
            create,
            queue=QUEUE_DODO,
            timeout=15,
        )

async def create_queue(queue_name: str):
    """создание очереди"""
    async with broker:
        await broker.declare_queue(RabbitQueue(queue_name))