from app.domain.value_objects.value_object import ValueObject


class ReturnDueDate(ValueObject):
    value: str

    @classmethod
    def create(cls) -> "ReturnDueDate":
        return ReturnDueDate(value="2021-06-30")
