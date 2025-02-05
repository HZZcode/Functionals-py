from typing import TypeVar, Callable

F = TypeVar('F', bound = Callable)

def Repeat(times: int) -> Callable[[F], F]:
    def repeater(f: F) -> F:
        def f_repeated(*args, **kwargs):
            ans = None
            for i in range(times):
                ans = f(*args, **kwargs)
            return ans
        return f_repeated
    return repeater