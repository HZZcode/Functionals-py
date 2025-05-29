from dataclasses import dataclass
from typing import Generic, TypeVar, Callable, TypeAlias

T = TypeVar('T')
F: TypeAlias = Callable[[T], bool]


@dataclass
class Predicate(Generic[T]):
    predicate: F

    def __call__(self, t: T) -> bool:
        return self.predicate(t)

    def __and__(self, other: F) -> 'Predicate[T]':
        return Predicate(lambda t: (self(t) and other(t)))

    def __or__(self, other: F) -> 'Predicate[T]':
        return Predicate(lambda t: (self(t) or other(t)))

    def __rand__(self, other: F) -> 'Predicate[T]':
        return Predicate(lambda t: (self(t) and other(t)))

    def __ror__(self, other: F) -> 'Predicate[T]':
        return Predicate(lambda t: (self(t) or other(t)))

    def __invert__(self) -> 'Predicate[T]':
        return Predicate(lambda t: not self(t))
