from typing import List

from app.domain.value_objects.movie.movie import Movie, ReleaseNote
from app.domain.value_objects.rental.fee import Fee

MOVEI_FEE = {
    ReleaseNote.NEW: 200,
    ReleaseNote.SEMI_NEW: 150,
    ReleaseNote.OLD: 100,
}


class RentalFeeCaluculator:
    @staticmethod
    def calculate(movies: List[Movie]) -> Fee:
        fee = 0
        for movie in movies:
            fee += MOVEI_FEE[movie.release_note]
        return Fee(value=fee)
