from abc import ABC, abstractclassmethod

from app.usecases.movies.get_movies_by_ids.input_port import GetMoviesByIdsInputPort
from app.usecases.movies.get_movies_by_ids.output_port import GetMoviesByIdsOutputPort


class GetMoviesByIdsUseCase(ABC):
    @abstractclassmethod
    def handle(self, input: GetMoviesByIdsInputPort) -> GetMoviesByIdsOutputPort:
        raise NotImplementedError
