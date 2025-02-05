from typing import TypeVar, Callable, Any

T = TypeVar('T', bound = Callable[..., Any])

def Repeat(times: int) -> Callable[[T], T]:
    def repeater(f: T) -> T:
        def f_repeated(*args, **kwargs):
            ans = None
            for i in range(times):
                ans = f(*args, **kwargs)
            return ans
        return f_repeated
    return repeater