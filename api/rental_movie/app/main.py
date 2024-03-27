from logging import getLogger

from app.interfaces.controllers.movie_controller import MovieController
from app.usecases.movie.rental.interactor import RentalMoviesInteractor
from fastapi import FastAPI

logger = getLogger("uvicorn.app")
app = FastAPI()


controller = MovieController(
    rental_usecase=RentalMoviesInteractor(),
)


@app.post("/")
async def test():
    return {"message": "Hello World!"}


@app.post("/rentals")
async def rental_movie(request: dict):
    response = controller.rental_movies()
    return response
