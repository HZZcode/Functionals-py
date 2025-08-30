from dataclasses import dataclass
from typing import Callable, Self


@dataclass
class Predicate[T]:
    predicate: Callable[[T], bool]

    def __call__(self, t: T) -> bool:
        return self.predicate(t)

    def __and__(self, other: Callable[[T], bool]):
        return Predicate[T](lambda t: (self(t) and other(t)))

    def __or__(self, other: Callable[[T], bool]):
        return Predicate[T](lambda t: (self(t) or other(t)))

    def __rand__(self, other: Callable[[T], bool]):
        return Predicate[T](lambda t: (self(t) and other(t)))

    def __ror__(self, other: Callable[[T], bool]):
        return Predicate[T](lambda t: (self(t) or other(t)))

    def __invert__(self):
        return Predicate[T](lambda t: not self(t))
