import time
from dataclasses import dataclass
from functools import wraps
from typing import TypeVar, Callable, Any

F = TypeVar('F', bound=Callable)


@dataclass
class CallData:
    count: int


call_counts: dict[str, CallData] = {}


def DebugArgs(interval: int = 1):
    def debugger(f: F) -> F:
        @wraps(f)
        def f_debugged(*args: Any, **kwargs: dict[str, Any]):
            name: str = f.__name__
            if name not in call_counts:
                call_counts[name] = CallData(0)
            count: int = call_counts[name].count + 1
            start: float = time.time()
            result = f(*args, **kwargs)
            end: float = time.time()
            if count % interval == 0:
                cost = end - start
                print(f'No.{count} call of func {name}, cost {cost:.3f}s'
                      + f', with {args=} and {kwargs=}')
            call_counts[name].count = count
            return result

        return f_debugged

    return debugger
