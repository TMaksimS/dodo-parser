"""pydantic schemas"""
import uuid

from pydantic import BaseModel

class DodoProduct(BaseModel):
    """Схема товара"""
    id: uuid.UUID
    name: str
    description: str
    section: str
    size: list[int] | None
    price: int
    images: list[str]