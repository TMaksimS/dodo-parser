"""pydantic schemas"""
import uuid

from pydantic import BaseModel

class DodoProductSchema(BaseModel):
    """Схема товара"""
    item_id: uuid.UUID
    name: str
    description: str
    section: str
    size: list[int] | None
    price: int
    images: list[str]
    city_link: str
