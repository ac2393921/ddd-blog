from typing import List

from app.intarfaces.controllers.movie_use_case_bus import MovieUseCaseBus
from app.usecases.movies.get_movies_by_ids.input_port import GetMoviesByIdsInputPort


class MovieController:
    def __init__(self, movie_use_case_bus: MovieUseCaseBus):
        self._bus = movie_use_case_bus

    def get_movies_by_ids(self, movie_ids: List[int]):
        input = GetMoviesByIdsInputPort(movie_ids=movie_ids)
        response = self._bus.handle(input)
        return response
