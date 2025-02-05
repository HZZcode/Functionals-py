import threading
from time import sleep
from typing import Callable, TypeVar

def singleton(cls):
    _instance = {}
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

@singleton
class TimeReachLimitType:
    def __str__(self):
        return "Time Reached Limit"

TimeReachLimit = TimeReachLimitType()

F = TypeVar('F', bound = Callable)

def TimeLimit(seconds: float) -> Callable[[F], F]:
    def limiter(f: F) -> F:
        def f_limited(*args, **kwargs):
            class CalcThread(threading.Thread):
                def __init__(self):
                    self.ans = TimeReachLimit
                    super().__init__()
                def run(self):
                    self.ans = f(*args, **kwargs)
            calc_thread = CalcThread()
            calc_thread.start()
            class LimitThread(threading.Thread):
                def __init__(self):
                    super().__init__()
                def run(self):
                    sleep(seconds)
            limit_thread = LimitThread()
            limit_thread.start()
            limit_thread.join()
            return calc_thread.ans
        return f_limited
    return limiter