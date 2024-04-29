from app.database import Base
from sqlalchemy import Column, DateTime, Enum, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from app.models.mixins import TimestampMixin
import enum
from app.models.rental_movies import RentalMovie


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
    fee = Column(Integer, nullable=False, comment="料金")
    movies = relationship(
        "Movie", secondary=RentalMovie.__tablename__, back_populates="rentals"
    )
