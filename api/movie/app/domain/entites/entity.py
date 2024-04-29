from abc import ABC, abstractclassmethod

from pydantic import BaseModel


class Entity(BaseModel, ABC):
    @abstractclassmethod
    def create(self):
        raise NotImplementedError

    @abstractclassmethod
    def reconstruct(self):
        raise NotImplementedError
