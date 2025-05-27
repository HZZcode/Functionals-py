from functools import reduce
from itertools import product, zip_longest, chain
from operator import mul
from typing import Sized, Iterable, Iterator, Callable, Any


def sized_iter(*, required_kwargs: dict[str, Any] | None = None,
               iter_getter: Callable[..., Iterator] = lambda *_, **__: iter([]),
               calc_size: Callable[..., int] = lambda *_, **__: 0) -> type:
    if required_kwargs is None:
        required_kwargs = {}

    class sized(Sized, Iterable):
        iterables: tuple[Iterable, ...]
        kwargs: dict[str, Any]
        inner_iter: Iterator
        size: int | None

        def __init__(self, *iterables: Iterable, **kwargs: dict[str, Any]):
            self.iterables = iterables
            self.kwargs = {**required_kwargs, **kwargs}
            self.inner_iter = iter_getter(*iterables, **kwargs)
            self.size = None

        def __iter__(self) -> Iterator:
            return self.inner_iter

        def __len__(self) -> int:
            return calc_size(self.iterables, **self.kwargs)

    return sized


sized_product = sized_iter(
    required_kwargs={'repeat': 1},
    iter_getter=product,
    calc_size=lambda iterables, repeat: reduce(mul, (len(list(iterable)) for iterable in iterables), 1) ** repeat
)
sized_zip = sized_iter(
    iter_getter=zip,
    calc_size=lambda iterables: min(len(list(iterable)) for iterable in iterables)
)
sized_zip_longest = sized_iter(
    iter_getter=zip_longest,
    calc_size=lambda iterables: max(len(list(iterable)) for iterable in iterables)
)
sized_chain = sized_iter(
    iter_getter=chain,
    calc_size=lambda iterables: sum(len(list(iterable)) for iterable in iterables)
)