from typing import List

from pydantic import BaseModel


class RentalMoviesInputPort(BaseModel):
    movie_id_list: List[str]
    user_id: int
