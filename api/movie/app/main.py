from app.infrastructures.gateway.grpc.server import GrpcServer
from app.intarfaces.controllers.movie_controller import MovieController
from app.intarfaces.controllers.movie_use_case_bus import MovieUseCaseBus


def main():
    server = GrpcServer(
        movie_controller=MovieController(
            movie_use_case_bus=MovieUseCaseBus(),
        )
    )
    server.run()


if __name__ == "__main__":
    main()
