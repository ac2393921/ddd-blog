from app.usecases.output_port import OutputPort


class GetMoviesByIdsOutputPort(OutputPort):
    movies: list[dict]
