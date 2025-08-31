from functools import wraps
from itertools import count
from time import sleep
from typing import Callable


def AutoRetry(except_type: type = Exception, /, max_retry: int | None = None,
              info_interval: int = 1, show_info: bool = True, retry_delay: float = 0):
    def retry[F: Callable](f: F) -> F:
        @wraps(f)
        def f_retry(*args, **kwargs):
            exception = None
            for retry_count in count(start=0) if max_retry is None else range(max_retry):
                try:
                    return f(*args, **kwargs)
                except except_type as e:
                    exception = e
                    if show_info and retry_count % info_interval == 0:
                        print(f'No.{retry_count + 1} retry of {f.__name__}')
                    sleep(retry_delay)
            if exception is not None:
                raise exception

        return f_retry

    return retry
