from unittest.mock import Mock

import pytest
from app.interfaces.controllers.movie_controller import MovieController
from app.usecases.movie.rental.input_port import RentalMoviesInputPort
from app.usecases.movie.rental.output_port import RentalMoviesOutputPort
from app.usecases.movie.rental.usecase import RentalMoviesUseCase


@pytest.fixture
def mock_rental_usecase():
    return Mock(spec=RentalMoviesUseCase)


def test_rental_movies(mock_rental_usecase):
    movie_controller = MovieController(rental_usecase=mock_rental_usecase)
    expected_input_port = RentalMoviesInputPort(movie_id=1, user_id=1)
    expected_output_port = RentalMoviesOutputPort(movie_id=1, user_id=1)
    mock_rental_usecase.handle.return_value = expected_output_port
    expected = expected_output_port.model_dump_json()

    actual = movie_controller.rental_movies()

    mock_rental_usecase.handle.assert_called_once_with(expected_input_port)
    assert actual == expected
