from app.domain.entities.rental import Rental
from app.domain.repositories.rental.i_rental_repository import IRentalRepository


class MockRentalRepository(IRentalRepository):
    def save(self, rental: Rental) -> None:
        print("save rental")
