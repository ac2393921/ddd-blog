from pydantic import BaseModel


class RentalMoviesInputPort(BaseModel):
    movie_id: int
    user_id: int
