from app.domain.value_objects.rental.rental_status import RentalStatus, RentalStatusType


def test_create():
    actual = RentalStatus(value=RentalStatusType.RENTAL)

    rental = RentalStatus.create()

    assert actual == rental
