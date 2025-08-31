from typing import Iterable


def auto_sum[T](iterable: Iterable[T]) -> T:
    iterator = iter(iterable)
    first = next(iterator, None)
    return sum(iterator, first) if first is not None else None
