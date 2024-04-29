from sqlalchemy import Column, ForeignKey
from sqlalchemy_utils import UUIDType
from app.database import Base


class RentalMovie(Base):
    __tablename__ = "rental_movie"
    __table_args__ = {"comment": "レンタル映画情報"}

    rental_id = Column(
        UUIDType(binary=False),
        ForeignKey("rentals.id"),
        primary_key=True,
        comment="レンタルID",
    )
    movie_id = Column(
        UUIDType(binary=False),
        ForeignKey("movies.id"),
        primary_key=True,
        comment="映画ID",
    )
