from enum import Enum

from app.domain.value_objects.movie.movie_id import MovieId
from app.domain.value_objects.value_object import ValueObject


class ReleaseNote(Enum):
    NEW = "new"
    SEMI_NEW = "semi_new"
    OLD = "old"


class Movie(ValueObject):
    movie_id: MovieId
    release_note: ReleaseNote

    def get_movie_id(self) -> MovieId:
        return self.movie_id

    def get_release_note(self) -> ReleaseNote:
        return self.release_note
