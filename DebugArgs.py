import time
from dataclasses import dataclass
from functools import wraps
from typing import TypeVar, Callable, Any

F = TypeVar('F', bound=Callable)


@dataclass
class CallData:
    count: int
    previous_time: float


call_counts: dict[F, CallData] = {}


def DebugArgs(interval: int = 1):
    def debugger(f: F) -> F:
        @wraps(f)
        def f_debugged(*args: Any, **kwargs: dict[str, Any]):
            if f not in call_counts:
                call_counts[f] = CallData(0, time.time())
            count: int = call_counts[f].count + 1
            if count % interval == 0:
                now: float = time.time()
                average = (now - call_counts[f].previous_time) / interval if f in call_counts else 0
                print(f'No. {count} call of func {f.__name__}, average cost {average:.3f}s per call'
                      + f', with {args=} and {kwargs=}')
                call_counts[f].previous_time = now
            call_counts[f].count = count
            return f(*args, **kwargs)

        return f_debugged

    return debugger
