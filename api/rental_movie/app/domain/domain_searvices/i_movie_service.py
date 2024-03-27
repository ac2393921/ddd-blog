from abc import ABC, abstractmethod
from typing import List

from app.domain.value_objects.movie.movie import Movie


class IMovieService(ABC):
    @abstractmethod
    def find_by_id(self, movie_id: str):
        raise NotImplementedError

    @abstractmethod
    def fetch_by_ids(self, movie_ids: List[str]) -> List[Movie]:
        raise NotImplementedError
