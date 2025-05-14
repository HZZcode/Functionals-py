from typing import TypeVar, Callable

F = TypeVar('F', bound = Callable)

def Currying(f: F):
    def f_curry(*args, **kwargs):
        if not args and not kwargs:
            return f_curry
        try:
            return f(*args, **kwargs)
        except TypeError:
            def new_f_curry(*next_args, **next_kwargs):
                return f_curry(*(args + next_args), **{**kwargs, **next_kwargs})
            return new_f_curry
    return f_curry