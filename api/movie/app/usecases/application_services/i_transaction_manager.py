from abc import ABC, abstractclassmethod


class ITransactionManager(ABC):
    @abstractclassmethod
    def begin(self):
        raise NotImplementedError
