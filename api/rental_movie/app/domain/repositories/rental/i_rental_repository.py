from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.rental import Rental


class IRentalRepository(ABC):
    @abstractmethod
    def save(self, rental: Rental) -> None:
        raise NotImplementedError
