from abc import ABC, abstractclassmethod


class SQLHandler(ABC):
    @abstractclassmethod
    def begin(self):
        raise NotImplementedError

    @abstractclassmethod
    def close(self):
        raise NotImplementedError

    @abstractclassmethod
    def commit(self):
        raise NotImplementedError

    @abstractclassmethod
    def rollback(self):
        raise NotImplementedError
