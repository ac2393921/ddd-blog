from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.rental import Rental


class IRentalRepository(ABC):
    @abstractmethod
    def fetch_by_user_id(self, user_id: int) -> List[Rental]:
        raise NotImplementedError
