from app.usecases.movies.get_movies_by_ids.input_port import GetMoviesByIdsInputPort
from app.usecases.movies.get_movies_by_ids.output_port import GetMoviesByIdsOutputPort
from app.usecases.movies.get_movies_by_ids.use_case import GetMoviesByIdsUseCase


class GetMoviesByIdsInteractor(GetMoviesByIdsUseCase):
    def handle(self, input: GetMoviesByIdsInputPort) -> GetMoviesByIdsOutputPort:
        return GetMoviesByIdsOutputPort(
            movies=[
                {"id": "1", "title": "The Shawshank Redemption", "rental_type": "new"},
                {"id": "2", "title": "The Godfather", "rental_type": "old"},
            ]
        )
