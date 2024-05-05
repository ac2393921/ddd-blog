from app.usecases.movie.rental.input_port import RentalMoviesInputPort
from app.usecases.movie.rental.usecase import RentalMoviesUseCase


class MovieController:
    def __init__(
        self,
        rental_usecase: RentalMoviesUseCase,
    ) -> None:
        self._rental_usecase = rental_usecase

    def rental_movies(self):
        input_port = RentalMoviesInputPort(
            movie_id_list=["0d721f33485c4ffdbfacc45606b1e2f4"],
            user_id="user_id",
        )
        response = self._rental_usecase.handle(input_port)
        return response.model_dump_json()
