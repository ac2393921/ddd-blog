from app.domain.repositories.i_movie_repository import IMovieRepository
from app.domain.value_objects.movies.movie_id import MovieId
from app.usecases.application_services.i_transaction_manager import ITransactionManager
from app.usecases.movies.get_movies_by_ids.input_port import GetMoviesByIdsInputPort
from app.usecases.movies.get_movies_by_ids.output_port import GetMoviesByIdsOutputPort
from app.usecases.movies.get_movies_by_ids.use_case import GetMoviesByIdsUseCase


class GetMoviesByIdsInteractor(GetMoviesByIdsUseCase):
    def __init__(
        self,
        transaction_manager: ITransactionManager,
        movie_repository: IMovieRepository,
    ) -> None:
        self._transaction_manager = transaction_manager
        self._movie_repository = movie_repository

    def handle(self, input: GetMoviesByIdsInputPort) -> GetMoviesByIdsOutputPort:
        with self._transaction_manager.begin() as session:
            movie_ids = [MovieId(value=movie_id) for movie_id in input.movie_ids]
            movies = self._movie_repository.get_by_ids(movie_ids, session)

        return GetMoviesByIdsOutputPort(
            movies=[
                {
                    "id": movie.movie_id.value,
                    "title": movie.title,
                    "rental_type": movie.rental_type.value,
                }
                for movie in movies
            ]
        )
