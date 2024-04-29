from uuid import UUID

from app.domain.exception import DomainException
from app.domain.value_objects.velue_object import ValueObject
from pydantic import field_validator


class MovieId(ValueObject):
    value: str

    @field_validator("value")
    def validate_movie_id(cls, v):
        try:
            UUID(v, version=4)
            return v
        except ValueError:
            raise DomainException("不正な値です。")
