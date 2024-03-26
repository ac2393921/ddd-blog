from app.usecases.movie.rental.input_port import RentalMoviesInputPort
from app.usecases.movie.rental.output_port import RentalMoviesOutputPort
from app.usecases.movie.rental.usecase import RentalMoviesUseCase


class RentalMoviesInteractor(RentalMoviesUseCase):
    def handle(self, input_port: RentalMoviesInputPort) -> RentalMoviesOutputPort:
        return RentalMoviesOutputPort(
            movie_id=input_port.movie_id, user_id=input_port.user_id
        )
