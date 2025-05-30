import itertools
from functools import wraps
from time import sleep
from typing import TypeVar, Callable, Iterable

F = TypeVar('F', bound=Callable)

def AutoRetry(except_type: type = Exception, max_retry: int | None = None,
              info_interval: int = 1, retry_delay: float = 0):
    def retry(f: F) -> F:
        it: Iterable
        if max_retry is None:
            it = itertools.count(start=0)
        @wraps(f)
        def f_retry(*args, **kwargs):
            for retry_count in it:
                try:
                    return f(*args, **kwargs)
                except except_type:
                    if retry_count % info_interval == 0:
                        print(f'No.{retry_count + 1} retry of {f.__name__}')
                    sleep(retry_delay)
        return f_retry
    return retry