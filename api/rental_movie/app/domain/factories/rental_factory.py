import uuid
from typing import List

from app.domain.domain_searvices.i_movie_service import IMovieService
from app.domain.domain_searvices.rental_due_date_calculator import (
    RentalDueDateCalculator,
)
from app.domain.entities.rental import Rental
from app.domain.exception.domain_exception import DomainException
from app.domain.repositories.rental.i_rental_repository import IRentalRepository
from app.domain.value_objects.movie.movie import Movie
from app.domain.value_objects.rental.rental_id import RentalId
from app.domain.value_objects.rental.user_id import UserId


class RentalFactory:
    def __init__(
        self, rental_repository: IRentalRepository, movie_service: IMovieService
    ):
        self._rental_repository = rental_repository
        self._movie_service = movie_service

    def create(self, user_id, movies: List[Movie]) -> Rental:
        if not movies:
            raise DomainException("映画がありません。")

        for movie in movies:
            rental_due_date = RentalDueDateCalculator.calculate(
                movie.get_release_note()
            )

        movie_id_list = [movie.get_movie_id() for movie in movies]

        return Rental.create(
            rental_id=RentalId(value=str(uuid.uuid4())),
            user_id=UserId(value=user_id),
            movie_id_list=movie_id_list,
            return_due_date=rental_due_date,
        )
