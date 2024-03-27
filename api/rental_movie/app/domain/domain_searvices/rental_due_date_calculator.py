from datetime import datetime, timedelta

from app.domain.value_objects.movie.movie import ReleaseNote

MOVIE_TYPE_DAYS = {
    ReleaseNote.NEW: 1,
    ReleaseNote.SEMI_NEW: 3,
    ReleaseNote.OLD: 7,
}


class RentalDueDateCalculator:
    @staticmethod
    def calculate(movie_type: ReleaseNote) -> str:
        return (datetime.now() + timedelta(days=MOVIE_TYPE_DAYS[movie_type])).strftime(
            "%Y-%m-%d"
        )
