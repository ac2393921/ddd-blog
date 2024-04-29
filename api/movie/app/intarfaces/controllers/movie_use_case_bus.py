from app.usecases.input_port import InputPort
from app.usecases.movies.get_movies_by_ids.input_port import GetMoviesByIdsInputPort
from app.usecases.movies.get_movies_by_ids.interactor import GetMoviesByIdsInteractor
from app.usecases.movies.get_movies_by_ids.output_port import GetMoviesByIdsOutputPort
from app.usecases.output_port import OutputPort


class MovieUseCaseBus:
    def handle(self, input: InputPort) -> OutputPort:
        if isinstance(input, GetMoviesByIdsInputPort):
            return GetMoviesByIdsInteractor().handle(input)
