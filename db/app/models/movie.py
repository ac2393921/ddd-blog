from app.database import Base
from sqlalchemy import Column, String, Enum
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from app.models.mixins import TimestampMixin
import enum


class RentalType(enum.Enum):
    NEW_RELEASE = "新作"
    SEMI_NEW_RELEASE = "準新作"
    OLD_RELEASE = "旧作"


class Movie(Base, TimestampMixin):
    __tablename__ = "movies"
    __table_args__ = {"comment": "映画情報"}

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid4, comment="ID")
    title = Column(String(255), nullable=False, comment="タイトル")
    rental_type = Column(Enum(RentalType), nullable=False, comment="レンタルタイプ")
