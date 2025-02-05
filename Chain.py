from typing import TypeVar, Callable, Any

C = TypeVar('C', bound = Any)
T = TypeVar('T', bound = Callable[[C], C])

def Chain(times: int) -> Callable[[T], T]:
    def chainer(f: T) -> T:
        def f_chain(arg: C) -> C:
            ans = arg
            for i in range(times):
                ans = f(ans)
            return ans
        return f_chain
    return chainer