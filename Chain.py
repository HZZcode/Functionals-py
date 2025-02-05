from typing import TypeVar, Callable, Any

C = TypeVar('C', bound = Any)
T = TypeVar('T', bound = Callable[[C], Any])

def Chain(times: int) -> Callable[[T], T]:
    def chainer(f: T) -> T:
        def f_chain(arg):
            ans = arg
            for i in range(times):
                ans = f(ans)
            return ans
        return f_chain
    return chainer