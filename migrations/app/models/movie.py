import enum
from uuid import uuid4

from app.database import Base
from app.models.mixins import TimestampMixin
from app.models.rental_movies import RentalMovie
from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType


class RentalType(enum.Enum):
    NEW_RELEASE = "new"
    SEMI_NEW_RELEASE = "semi_new"
    OLD_RELEASE = "old"


class Movie(Base, TimestampMixin):
    __tablename__ = "movies"
    __table_args__ = {"comment": "映画情報"}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4, comment="ID")
    title = Column(String(255), nullable=False, comment="タイトル")
    rental_type = Column(Enum(RentalType), nullable=False, comment="レンタルタイプ")

    rentals = relationship(
        "Rental", secondary=RentalMovie.__tablename__, back_populates="movies"
    )
