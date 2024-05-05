from app.config import mysql_settings
from app.infrastructures.data_store.application_services.sql_transaction_manager import (
    SQLTransactionManager,
)
from app.infrastructures.data_store.handler.mysql_handler import MySQLHandler
from app.infrastructures.data_store.repositories.movies.mysql_movie_repository import (
    MySQLMovieRepository,
)
from app.infrastructures.gateway.grpc.server import GrpcServer
from app.intarfaces.controllers.movie_controller import MovieController
from app.intarfaces.controllers.movie_use_case_bus import MovieUseCaseBus


def main():
    server = GrpcServer(
        movie_controller=MovieController(
            movie_use_case_bus=MovieUseCaseBus(
                transaction_manager=SQLTransactionManager(
                    handler=MySQLHandler(
                        host=mysql_settings.MYSQL_HOST,
                        user=mysql_settings.MYSQL_USER,
                        password=mysql_settings.MYSQL_PASSWORD,
                        database=mysql_settings.MYSQL_DATABASE,
                    )
                ),
                movie_repository=MySQLMovieRepository(
                    handler=MySQLHandler(
                        host=mysql_settings.MYSQL_HOST,
                        user=mysql_settings.MYSQL_USER,
                        password=mysql_settings.MYSQL_PASSWORD,
                        database=mysql_settings.MYSQL_DATABASE,
                    )
                ),
            )
        )
    )
    server.run()


if __name__ == "__main__":
    main()
