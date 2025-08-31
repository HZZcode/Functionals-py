from typing import Iterable


def auto_sum[T](iterable: Iterable[T]) -> T:
    iterator = iter(iterable)
    return sum(iterator, next(iterator, None))
