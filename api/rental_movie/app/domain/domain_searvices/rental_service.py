from typing import List

from app.domain.constants import MAX_RENTAL_MOVIE
from app.domain.exception.domain_exception import DomainException
from app.domain.repositories.rental.i_rental_repository import IRentalRepository


class RentalService:
    def __init__(self, rental_repository: IRentalRepository):
        self._rental_repository = rental_repository

    def check_rental_limit_exceeded(self, user_id: int, movie_id_list: List[str]):
        # レンタル可能本数を超えている場合はエラー
        if len(movie_id_list) > MAX_RENTAL_MOVIE:
            raise DomainException("レンタル可能本数を超えています。")

        # すでにレンタル済みの本数と合わせてレンタル可能本数を超えていないかチェック
        rentals = self._rental_repository.fetch_by_user_id(user_id)
        rentaled_movies = []
        for rental in rentals:
            rentaled_movies += rental.get_movie_id_list()
        if len(rentaled_movies) + len(movie_id_list) > MAX_RENTAL_MOVIE:
            raise DomainException("レンタル可能本数を超えています。")
