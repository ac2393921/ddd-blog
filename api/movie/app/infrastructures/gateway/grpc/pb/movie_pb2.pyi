from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Movie(_message.Message):
    __slots__ = ("id", "title", "rental_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    RENTAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    rental_type: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., rental_type: _Optional[str] = ...) -> None: ...

class GetByIdsRequest(_message.Message):
    __slots__ = ("movie_ids",)
    MOVIE_IDS_FIELD_NUMBER: _ClassVar[int]
    movie_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, movie_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class GetByIdRequest(_message.Message):
    __slots__ = ("movie_id",)
    MOVIE_ID_FIELD_NUMBER: _ClassVar[int]
    movie_id: int
    def __init__(self, movie_id: _Optional[int] = ...) -> None: ...
