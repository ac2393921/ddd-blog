import enum
from uuid import uuid4

from app.database import Base
from app.models.mixins import TimestampMixin
from app.models.rental_movies import RentalMovie
from sqlalchemy import Column, DateTime, Enum, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType


class RentalStatusType(enum.Enum):
    RENTAL = "rental"
    RETURNED = "returned"
    OVERDUE = "overdue"


class Rental(Base, TimestampMixin):
    __tablename__ = "rentals"
    __table_args__ = {"comment": "レンタル情報"}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4, comment="ID")
    rental_date = Column(DateTime, nullable=False, comment="レンタル日")
    return_due_date = Column(DateTime, nullable=False, comment="返却期限日")
    retrun_date = Column(DateTime, nullable=True, comment="返却日")
    rental_status = Column(
        Enum(RentalStatusType), nullable=False, comment="レンタルステータス"
    )
    movies = relationship(
        "Movie", secondary=RentalMovie.__tablename__, back_populates="rentals"
    )
