from functools import wraps
from typing import TypeVar, Callable, Iterable, Any


def Repeat[F: Callable](times: int) -> Callable[[F], F]:
    def repeater(f: F) -> F:
        @wraps(f)
        def f_repeated(*args, **kwargs):
            ans = None
            for i in range(times):
                ans = f(*args, **kwargs)
            return ans

        return f_repeated

    return repeater
