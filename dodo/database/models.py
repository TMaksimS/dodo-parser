"""db models"""
import uuid

from sqlalchemy import UUID, String, ARRAY, Integer
from sqlalchemy.orm import mapped_column, Mapped

from dodo.database import Base


class DodoProductModel(Base):
    """Обьект продукции ДОДО"""
    __tablename__ = "dodo_products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    item_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    section: Mapped[str] = mapped_column(String)
    size: Mapped[list[int]] = mapped_column(ARRAY(Integer), nullable=True)
    price: Mapped[int] = mapped_column(Integer)
    images: Mapped[list[str]] = mapped_column(ARRAY(String))
    city_link: Mapped[str] = mapped_column(String)