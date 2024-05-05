from logging import getLogger

from app.infrastructures.data_source.domain_services.movie.mock_movie_service import (
    MockMovieService,
)
from app.infrastructures.data_source.repositories.rental.mock_rental_repository import (
    MockRentalRepository,
)
from app.interfaces.controllers.movie_controller import MovieController
from app.usecases.movie.rental.interactor import RentalMoviesInteractor
from fastapi import FastAPI

logger = getLogger("uvicorn.app")
app = FastAPI()


controller = MovieController(
    rental_usecase=RentalMoviesInteractor(
        rental_repository=MockRentalRepository(),
        movie_service=MockMovieService(),
    ),
)


@app.post("/")
async def test():
    return {"message": "Hello World!"}


@app.post("/rentals")
async def rental_movie(request: dict):
    response = controller.rental_movies()
    return response
