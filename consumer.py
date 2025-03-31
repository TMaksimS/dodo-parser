"""main file for consumer"""
# pylint: disable = [import-error, no-name-in-module, broad-exception-caught, broad-exception-raised, raise-missing-from, no-member]

import asyncio

from aiormq import AMQPConnectionError
from faststream.annotations import FastStream

from dodo.database.models import DodoProductModel
from dodo.database.uow import UoW
from dodo.dodo.config import QUEUE_DODO
from dodo.dodo.logger import LOGER
from dodo.dodo.rabbitmq.rabbit_broker import broker, create_queue
from dodo.dodo.rabbitmq.schemas import DodoProductSchema

app = FastStream(broker)

@LOGER.catch
@broker.subscriber(QUEUE_DODO)
async def save_products_into_db(body: DodoProductSchema):
    """for saving DodoProduct into database"""
    LOGER.info({"item_name": body.name, "status": "started to save"})
    try:
        result = await UoW().create_obj(DodoProductModel, **body.model_dump())
        if result:
            LOGER.info({"item_name": body.name, "status": "has been saved"})
            return True
    except Exception as e:
        LOGER.info({"item_name": body.name, "status": "failed"})
        LOGER.error(e)


if __name__ == "__main__":
    try:
        asyncio.run(create_queue(QUEUE_DODO))
    except AMQPConnectionError:
        raise Exception("Error when connecting to rabbit")
    LOGER.info("CONNECTED TO RABBIT")
    connection = asyncio.run(UoW().test_connect())
    if isinstance(connection, ConnectionRefusedError):
        raise Exception(f"Error when connecting to database: {connection}")
    LOGER.info("CONNECTED TO DATABASE")
    asyncio.run(app.run(sleep_time=5.0))
