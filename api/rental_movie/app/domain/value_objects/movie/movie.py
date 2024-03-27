from enum import Enum

from app.domain.value_objects.value_object import ValueObject


class ReleaseNote(Enum):
    NEW = "new"
    SEMI_NEW = "semi_new"
    OLD = "old"


class Movie(ValueObject):
    movie_id: str
    release_note: ReleaseNote
