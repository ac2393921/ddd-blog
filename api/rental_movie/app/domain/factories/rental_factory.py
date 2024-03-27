import uuid
from typing import List

from app.domain.domain_searvices.i_movie_service import IMovieService
from app.domain.domain_searvices.rental_due_date_calculator import (
    RentalDueDateCalculator,
)
from app.domain.domain_searvices.rental_fee_caluculator import RentalFeeCaluculator
from app.domain.entities.rental import Rental
from app.domain.repositories.rental.i_rental_repository import IRentalRepository
from app.domain.value_objects.movie.movie import Movie
from app.domain.value_objects.rental.rental_status import RentalStatus


class RentalFactory:
    def __init__(
        self, rental_repository: IRentalRepository, movie_service: IMovieService
    ):
        self._rental_repository = rental_repository
        self._movie_service = movie_service

    def create(self, user_id, movies: List[Movie]) -> Rental:
        for movie in movies:
            rental_due_date = RentalDueDateCalculator.calculate(movie)

        fee = RentalFeeCaluculator.calculate(movies)

        movie_id_list = [movie.get_movie_id() for movie in movies]

        return Rental(
            rental_id=str(uuid.uuid4()),
            user_id=user_id,
            movie_id_list=movie_id_list,
            return_due_date=rental_due_date,
            return_date=None,
            rental_status=RentalStatus.create(),
            fee=fee,
        )
