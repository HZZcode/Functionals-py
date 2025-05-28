import inspect
import time
from functools import wraps


def Timer(time_processor = None, avoid_recursive = True, show_args = False):
    def timer(f):
        @wraps(f)
        def f_timed(*args, **kwargs):
            start = time.time()
            result = f(*args, **kwargs)
            end = time.time()
            cost = end - start

            stack = inspect.stack()
            is_recursive = sum(1 for frame in stack if frame.function == f.__name__) > 0
            if not is_recursive and avoid_recursive:
                if time_processor is None:
                    args_str = '' if not show_args else f' with [{args=}, {kwargs=}]'
                    print(f'function{args_str} {f.__name__} cost {cost:.3f}s')
                else:
                    time_processor(cost)
            return result
        return f_timed
    return timer
