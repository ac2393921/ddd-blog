from abc import ABC, abstractclassmethod
from typing import List

from app.domain.entites.movie import Movie
from app.domain.value_objects.movies.movie_id import MovieId


class IMovieRepository(ABC):
    @abstractclassmethod
    def get_by_ids(self, movie_ids: List[MovieId]) -> List[Movie]:
        raise NotImplementedError
