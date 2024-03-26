from pydantic import BaseModel


class RentalMoviesOutputPort(BaseModel):
    movie_id: int
    user_id: int
