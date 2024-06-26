from concurrent import futures

import grpc
from app.intarfaces.controllers.movie_controller import MovieController
from grpc_reflection.v1alpha import reflection

from .pb import movie_pb2, movie_pb2_grpc


# レスポンスの処理
class MovieService(movie_pb2_grpc.MovieServiceServicer):
    def __init__(self, movie_controller: MovieController):
        self._movie_controller = movie_controller

    def GetByIds(self, request: movie_pb2.GetByIdRequest, context) -> movie_pb2.Movie:
        response = self._movie_controller.get_movies_by_ids(movie_ids=request.movie_ids)

        for movie in response.movies:
            print(movie)
            yield movie_pb2.Movie(
                id=str(movie["id"]),
                title=movie["title"],
                rental_type=movie["rental_type"],
            )

    def GetById(self, request, context):
        movie = movie_pb2.Movie(id="1", title="movie1", rental_type="new")
        return movie


class GrpcServer:
    def __init__(self, movie_controller: MovieController):
        self._port: str = "3001"
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self._movie_controller = movie_controller

    def run(self) -> None:
        movie_pb2_grpc.add_MovieServiceServicer_to_server(
            MovieService(movie_controller=self._movie_controller), self._server
        )

        SERVICE_NAMES = (
            movie_pb2.DESCRIPTOR.services_by_name["MovieService"].full_name,
            reflection.SERVICE_NAME,
        )
        # サーバーの立ち上げ
        self._server.add_insecure_port(f"[::]:{self._port}")
        self._server.start()
        print("server started")
        reflection.enable_server_reflection(SERVICE_NAMES, self._server)
        self._server.wait_for_termination()


if __name__ == "__main__":
    server = GrpcServer()
    server.run()
