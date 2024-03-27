import pytest
from app.domain.entities.rental import Rental
from app.domain.exception.domain_exception import DomainException
from app.domain.value_objects.rental.fee import Fee
from app.domain.value_objects.rental.movie_id import MovieId
from app.domain.value_objects.rental.rental_id import RentalId
from app.domain.value_objects.rental.rental_status import RentalStatus, RentalStatusType
from app.domain.value_objects.rental.user_id import UserId


def test_get_rental_id():
    expected = RentalId(value="11111")
    rental = Rental(
        rental_id=expected,
        user_id=UserId(value="22222"),
        movie_id_list=[MovieId(value="33333")],
        return_due_date="2021-01-01",
        return_date="2021-01-02",
        rental_status=RentalStatus(value=RentalStatusType.RENTAL),
        fee=Fee(value=1000),
    )

    actual = rental.get_rental_id()

    assert actual == expected


def test_get_movie_id_list():
    expected = [MovieId(value="33333"), MovieId(value="44444")]
    rental = Rental(
        rental_id=RentalId(value="11111"),
        user_id=UserId(value="22222"),
        movie_id_list=expected,
        return_due_date="2021-01-01",
        return_date="2021-01-02",
        rental_status=RentalStatus(value=RentalStatusType.RENTAL),
        fee=Fee(value=1000),
    )

    actual = rental.get_movie_id_list()

    assert actual == expected


def test_get_return_due_date():
    expected = "2021-01-01"
    rental = Rental(
        rental_id=RentalId(value="11111"),
        user_id=UserId(value="22222"),
        movie_id_list=[MovieId(value="33333")],
        return_due_date=expected,
        return_date="2021-01-02",
        rental_status=RentalStatus(value=RentalStatusType.RENTAL),
        fee=Fee(value=1000),
    )

    actual = rental.get_return_due_date()

    assert actual == expected


def test_get_return_date():
    expected = "2021-01-02"
    rental = Rental(
        rental_id=RentalId(value="11111"),
        user_id=UserId(value="22222"),
        movie_id_list=[MovieId(value="33333")],
        return_due_date="2021-01-01",
        return_date=expected,
        rental_status=RentalStatus(value=RentalStatusType.RENTAL),
        fee=Fee(value=1000),
    )

    actual = rental.get_return_date()

    assert actual == expected


def test_get_return_date_not_returned():
    rental = Rental(
        rental_id=RentalId(value="11111"),
        user_id=UserId(value="22222"),
        movie_id_list=[MovieId(value="33333")],
        return_due_date="2021-01-01",
        return_date=None,
        rental_status=RentalStatus(value=RentalStatusType.RENTAL),
        fee=Fee(value=1000),
    )

    with pytest.raises(DomainException) as _:
        rental.get_return_date()
        raise DomainException("Test domain exception")


def test_get_fee():
    expected = Fee(value=1000)
    rental = Rental(
        rental_id=RentalId(value="11111"),
        user_id=UserId(value="22222"),
        movie_id_list=[MovieId(value="33333")],
        return_due_date="2021-01-01",
        return_date=None,
        rental_status=RentalStatus(value=RentalStatusType.RENTAL),
        fee=expected,
    )

    actual = rental.get_fee()

    assert actual == expected


def test_is_return_returns_true_when_rental_is_returned():
    expect = True
    rental = Rental(
        rental_id=RentalId(value="11111"),
        user_id=UserId(value="22222"),
        movie_id_list=[MovieId(value="33333")],
        return_due_date="2021-01-01",
        return_date="2021-01-02",
        rental_status=RentalStatus(value=RentalStatusType.RETURNED),
        fee=Fee(value=1000),
    )

    actual = rental.is_return()

    return expect == actual


def test_is_return_returns_false_when_rental_is_not_returned():
    expect = False
    rental = Rental(
        rental_id=RentalId(value="11111"),
        user_id=UserId(value="22222"),
        movie_id_list=[MovieId(value="33333")],
        return_due_date="2021-01-01",
        return_date=None,
        rental_status=RentalStatus(value=RentalStatusType.RENTAL),
        fee=Fee(value=1000),
    )

    actual = rental.is_return()

    return expect == actual


def test_create():
    rental_id = "11111"
    return_due_date = "2021-01-01"
    fee = 1000
    expect = Rental(
        rental_id=RentalId(value=rental_id),
        user_id=UserId(value="22222"),
        movie_id_list=[MovieId(value="33333")],
        return_due_date=return_due_date,
        return_date=None,
        rental_status=RentalStatus(value=RentalStatusType.RENTAL),
        fee=Fee(value=fee),
    )

    actual = Rental.create(rental_id, return_due_date, fee)

    assert actual == expect
