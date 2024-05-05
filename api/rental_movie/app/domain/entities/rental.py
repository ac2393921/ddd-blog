from typing import List, Optional

from app.domain.entities.entity import Entity
from app.domain.exception.domain_exception import DomainException
from app.domain.value_objects.movie.movie_id import MovieId
from app.domain.value_objects.rental.rental_id import RentalId
from app.domain.value_objects.rental.rental_status import RentalStatus, RentalStatusType
from app.domain.value_objects.rental.user_id import UserId


class Rental(Entity):
    """レンタルエンティティ"""

    rental_id: RentalId
    user_id: UserId
    movie_id_list: List[MovieId]
    return_due_date: str
    return_date: Optional[str]
    rental_status: RentalStatus

    def get_rental_id(self) -> RentalId:
        return self.rental_id

    def get_movie_id_list(self) -> List[MovieId]:
        return self.movie_id_list

    def get_return_due_date(self) -> str:
        return self.return_due_date

    def get_return_date(self) -> str:
        if self.return_date is None:
            raise DomainException("まだ返却されていません。")
        return self.return_date

    def is_return(self) -> bool:
        return self.rental_status.value == RentalStatusType.RETURNED

    @classmethod
    def create(
        cls,
        rental_id: RentalId,
        user_id: UserId,
        movie_id_list: List[MovieId],
        return_due_date: str,
    ) -> "Rental":
        rental_status = RentalStatus.create()

        return Rental(
            rental_id=rental_id,
            user_id=user_id,
            movie_id_list=movie_id_list,
            return_due_date=return_due_date,
            return_date=None,
            rental_status=rental_status,
        )
