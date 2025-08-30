from functools import wraps
from typing import Callable


def Chain[T, F: Callable](times: int) -> Callable[[F], F]:
    def chainer(f: F) -> F:
        @wraps(f)
        def f_chain(arg: T) -> T:
            ans = arg
            for i in range(times):
                ans = f(ans)
            return ans

        return f_chain

    return chainer
