from abc import ABC, abstractmethod

from app.usecases.movie.rental.input_port import RentalMoviesInputPort
from app.usecases.movie.rental.output_port import RentalMoviesOutputPort


class RentalMoviesUseCase(ABC):
    @abstractmethod
    def handle(self, input_port: RentalMoviesInputPort) -> RentalMoviesOutputPort:
        raise NotImplementedError
