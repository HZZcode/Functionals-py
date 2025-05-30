from typing import Iterable

from typing_extensions import TypeVar

T = TypeVar('T')

def auto_sum(iterable: Iterable[T]) -> T:
    first = next(iter(iterable), None)
    if first is not None:
        return sum(iterable, type(first)())
    return sum(iterable)
# BUG: auto_sum(Iterator) ignores the first element