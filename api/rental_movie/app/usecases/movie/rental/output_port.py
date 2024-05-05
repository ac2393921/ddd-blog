from pydantic import BaseModel


class RentalMoviesOutputPort(BaseModel):
    rental_id: str
