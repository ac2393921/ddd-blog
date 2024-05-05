from typing import List

from app.domain.domain_searvices.i_movie_service import IMovieService
from app.domain.value_objects.movie.movie import Movie, ReleaseNote
from app.domain.value_objects.movie.movie_id import MovieId


class MockMovieService(IMovieService):
    def find_by_id(self, movie_id: str):
        pass

    def fetch_by_ids(self, movie_ids: List[str]) -> List[Movie]:
        print("fetch movies by ids")
        return [
            Movie(
                movie_id=MovieId(value="02686eccacd8473690556cfaa93df36b"),
                release_note=ReleaseNote("new"),
            )
        ]
