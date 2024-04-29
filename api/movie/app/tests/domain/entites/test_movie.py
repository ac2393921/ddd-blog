from uuid import uuid4

from app.domain.entites.movie import Movie, RentalType
from app.domain.value_objects.movies.movie_id import MovieId


def test_create_movie_correct():
    movie_id = MovieId(value=str(uuid4()))
    title = "title"
    actual = Movie(
        movie_id=movie_id,
        title=title,
        rental_type=RentalType.NEW_RELEASE,
    )

    expected = Movie.create(
        movie_id=movie_id,
        title=title,
        rental_type=RentalType.NEW_RELEASE,
    )

    assert expected.movie_id == actual.movie_id
    assert expected.title == actual.title
    assert expected.rental_type == actual.rental_type


def test_reconstruct_movie_correct():
    movie_id = MovieId(value=str(uuid4()))
    title = "title"
    actual = Movie(
        movie_id=movie_id,
        title=title,
        rental_type=RentalType.NEW_RELEASE,
    )

    expected = Movie.reconstruct(
        movie_id=movie_id,
        title=title,
        rental_type=RentalType.NEW_RELEASE,
    )

    assert expected.movie_id == actual.movie_id
    assert expected.title == actual.title
    assert expected.rental_type == actual.rental_type
