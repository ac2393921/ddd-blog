from typing import List

from app.domain.entites.movie import Movie, RentalType
from app.domain.repositories.i_movie_repository import IMovieRepository
from app.domain.value_objects.movies.movie_id import MovieId
from app.infrastructures.data_store.handler.mysql_handler import MySQLHandler
from sqlalchemy import text


class MySQLMovieRepository(IMovieRepository):
    def __init__(self, handler: MySQLHandler) -> None:
        self._handler = handler

    def get_by_ids(self, movie_ids: List[MovieId], session) -> List[Movie]:
        movie_id_values = [movie_id.value for movie_id in movie_ids]

        query = text("SELECT * FROM movies WHERE id IN :movie_ids")
        result = session.execute(query, {"movie_ids": movie_id_values})
        rows = result.fetchall()

        return [
            Movie.reconstruct(
                movie_id=MovieId(value=row.id),
                title=row.title,
                rental_type=RentalType[row.rental_type],
            )
            for row in rows
        ]
