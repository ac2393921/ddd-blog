from app.domain.repositories.i_movie_repository import IMovieRepository
from app.usecases.application_services.i_transaction_manager import ITransactionManager
from app.usecases.input_port import InputPort
from app.usecases.movies.get_movies_by_ids.input_port import GetMoviesByIdsInputPort
from app.usecases.movies.get_movies_by_ids.interactor import GetMoviesByIdsInteractor
from app.usecases.output_port import OutputPort


class MovieUseCaseBus:
    def __init__(
        self,
        transaction_manager: ITransactionManager,
        movie_repository: IMovieRepository,
    ) -> None:
        self._transaction_manager = transaction_manager
        self._movie_repository = movie_repository

    def handle(self, input: InputPort) -> OutputPort:
        if isinstance(input, GetMoviesByIdsInputPort):
            return GetMoviesByIdsInteractor(
                transaction_manager=self._transaction_manager,
                movie_repository=self._movie_repository,
            ).handle(input)
