from enum import Enum

from app.domain.value_objects.value_object import ValueObject


class RentalStatusType(Enum):
    RENTAL = "RENTAL"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"


class RentalStatus(ValueObject):
    value: RentalStatusType

    @classmethod
    def create(cls) -> "RentalStatus":
        return RentalStatus(value=RentalStatusType.RENTAL)
