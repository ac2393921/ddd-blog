from enum import Enum
from uuid import uuid4

from app.domain.entites.entity import Entity
from app.domain.value_objects.movies.movie_id import MovieId


class RentalType(Enum):
    NEW_RELEASE = "new"
    SEMI_NEW_RELEASE = "semi_new"
    OLD_RELEASE = "old"


class Movie(Entity):
    """映画エンティティ"""

    movie_id: MovieId
    title: str
    rental_type: RentalType

    @classmethod
    def create(self, movie_id: MovieId, title: str, rental_type: RentalType) -> "Movie":
        return Movie(
            movie_id=movie_id,
            title=title,
            rental_type=rental_type,
        )

    @classmethod
    def reconstruct(
        self, movie_id: MovieId, title: str, rental_type: RentalType
    ) -> "Movie":
        return Movie(
            movie_id=movie_id,
            title=title,
            rental_type=rental_type,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Movie):
            return False

        return self.movie_id == other.movie_id
