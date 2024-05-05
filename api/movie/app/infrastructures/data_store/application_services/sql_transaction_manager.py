from app.infrastructures.data_store.handler.sql_handler import SQLHandler
from app.usecases.application_services.i_transaction_manager import ITransactionManager


class SQLTransactionManager(ITransactionManager):
    def __init__(self, handler: SQLHandler) -> None:
        self._handler = handler

    def begin(self):
        return self._handler.begin()

    # def __enter__(self):
    #     self._handler.begin()

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if exc_type is None:
    #         self._handler.commit()
    #     else:
    #         self._handler.rollback()
    #     self._handler.close()
