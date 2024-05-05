from app.domain.domain_searvices.i_movie_service import IMovieService
from app.domain.domain_searvices.rental_service import RentalService
from app.domain.factories.rental_factory import RentalFactory
from app.domain.repositories.rental.i_rental_repository import IRentalRepository
from app.usecases.movie.rental.input_port import RentalMoviesInputPort
from app.usecases.movie.rental.output_port import RentalMoviesOutputPort
from app.usecases.movie.rental.usecase import RentalMoviesUseCase


class RentalMoviesInteractor(RentalMoviesUseCase):
    def __init__(
        self,
        rental_repository: IRentalRepository,
        movie_service: IMovieService,
        # user_service,
    ):
        self._rental_repository = rental_repository
        self._rental_service = RentalService(rental_repository=rental_repository)
        self._movie_service = movie_service
        # self._user_service = user_service
        self._movie_factory = RentalFactory(
            rental_repository=rental_repository, movie_service=movie_service
        )

    def handle(self, input_port: RentalMoviesInputPort) -> RentalMoviesOutputPort:
        # ユーザーの会員ステータスをチェック
        # self._user_service.check_user_status(user_id)

        # レンタル可能本数を超えていないかチェック
        # self._rental_service.check_rental_limit_exceeded(user_id=input_port.user_id)

        movies = self._movie_service.fetch_by_ids(input_port.movie_id_list)
        rental = self._movie_factory.create(
            user_id=input_port.user_id,
            movies=movies,
        )
        self._rental_repository.save(rental)

        return RentalMoviesOutputPort(
            rental_id=rental.get_rental_id().value,
        )
