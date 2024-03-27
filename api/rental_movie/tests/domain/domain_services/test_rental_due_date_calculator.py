from datetime import datetime, timedelta

from app.domain.domain_searvices.rental_due_date_calculator import (
    RentalDueDateCalculator,
)
from app.domain.value_objects.movie.movie import ReleaseNote


def test_caluculate(mocker):
    # datetime.now()をモックする
    # mock_datetime = mocker.Mock()
    # mock_datetime.now.return_value = datetime(2024, 4, 1, 0, 0, 0)
    # mocker.patch(
    #     "app.domain.domain_searvices.rental_due_date_calculator.datetime",
    #     return_value=mock_datetime,
    # )
    release_note = ReleaseNote.NEW
    # expected = "2024-04-02"
    expected = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    actual = RentalDueDateCalculator.calculate(release_note)

    assert actual == expected
