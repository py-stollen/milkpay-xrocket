from typing import Any, Generator, Generic, Optional, TypeVar

from .base import PayXRocketObject

T = TypeVar("T", bound=Any)


class Pagination(PayXRocketObject, Generic[T]):
    total: int
    limit: Optional[int] = None
    offset: Optional[int] = None
    results: list[T]

    def __iter__(self) -> Generator[T, None, None]:
        yield from self.results
