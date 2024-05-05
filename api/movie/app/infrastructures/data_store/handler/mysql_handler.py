import sqlalchemy
from app.infrastructures.data_store.handler.sql_handler import SQLHandler
from sqlalchemy.engine.base import Connection
from sqlalchemy.orm import sessionmaker


class MySQLHandler(SQLHandler):
    def __init__(self, host: str, user: str, password: str, database: str):
        self._engine = sqlalchemy.create_engine(
            "mysql://%s:%s@%s/%s?charset=utf8" % (user, password, host, database),
        )
        self._session = sessionmaker(bind=self._engine)

    def begin(self) -> Connection:
        return self._session.begin()

    def close(self):
        self._session.close()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
