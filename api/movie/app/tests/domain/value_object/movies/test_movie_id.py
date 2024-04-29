from uuid import uuid4

import pytest
from app.domain.exception import DomainException
from app.domain.value_objects.movies.movie_id import MovieId


def test_create_movie_id_correct():
    expected = str(uuid4())

    movie_id = MovieId(value=expected)

    actual = movie_id.value
    assert actual == expected


def test_validate_id():
    with pytest.raises(DomainException) as _:
        MovieId(value="invalid_id")
        raise DomainException("Test domain exception")
