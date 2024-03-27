from pydantic import BaseModel, ConfigDict


class ValueObject(BaseModel):
    model_config = ConfigDict(frozen=True)

    def __eq__(self, other: "ValueObject") -> bool:
        return isinstance(other, ValueObject) and self.value == other.value
