from app.usecases.input_port import InputPort


class GetMoviesByIdsInputPort(InputPort):
    movie_ids: list[int]
