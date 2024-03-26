from app.usecases.movie.rental.input_port import RentalMoviesInputPort
from app.usecases.movie.rental.interactor import RentalMoviesInteractor
from app.usecases.movie.rental.output_port import RentalMoviesOutputPort


def test_handle():
    usecase = RentalMoviesInteractor()
    input_port = RentalMoviesInputPort(movie_id=1, user_id=1)
    expected = RentalMoviesOutputPort(movie_id=1, user_id=1)

    actual = usecase.handle(input_port)

    assert actual == expected
