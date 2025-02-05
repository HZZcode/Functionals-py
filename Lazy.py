from typing import Any, Callable, TypeVar

T = TypeVar('T', bound = Any)
F0: TypeVar = Callable[[], T]
F: TypeVar = Callable[[...], T]

class LazyData:
    _func: F0
    _used: bool = False
    _value: T = None
    def __init__(self, func: F0):
        self._func = func
    def getValue(self):
        if not self._used:
            self._value = self._func()
            self._used = True
        return self._value

    def __getattribute__(self, name):
        if name not in ['_func', '_used', '_value', 'calc', '__getattribute__']:
            self.getValue()
            return self._value.__getattribute__(name)
        return super().__getattribute__(name)

    def __setattr__(self, key, value):
        if key not in ['_func', '_used', '_value', 'calc', '__getattribute__']:
            self.getValue()
            return self._value.__setattr__(key, value)
        return super().__setattr__(key, value)

    def __str__(self):
        self.getValue()
        return str(self._value)
    def __repr__(self):
        self.getValue()
        return repr(self._value)
    def __eq__(self, other):
        self.getValue()
        return self._value == other
    def __ne__(self, other):
        self.getValue()
        return self._value != other
    def __lt__(self, other):
        self.getValue()
        return self._value < other
    def __le__(self, other):
        self.getValue()
        return self._value <= other
    def __gt__(self, other):
        self.getValue()
        return self._value > other
    def __ge__(self, other):
        self.getValue()
        return self._value >= other
    def __add__(self, other):
        self.getValue()
        return self._value + other
    def __sub__(self, other):
        self.getValue()
        return self._value - other
    def __mul__(self, other):
        self.getValue()
        return self._value * other
    def __truediv__(self, other):
        self.getValue()
        return self._value / other
    def __floordiv__(self, other):
        self.getValue()
        return self._value // other
    def __mod__(self, other):
        self.getValue()
        return self._value % other
    def __pow__(self, other):
        self.getValue()
        return self._value ** other
    def __radd__(self, other):
        self.getValue()
        return other + self._value
    def __rsub__(self, other):
        self.getValue()
        return other - self._value
    def __rmul__(self, other):
        self.getValue()
        return other * self._value
    def __rtruediv__(self, other):
        self.getValue()
        return other / self._value
    def __rfloordiv__(self, other):
        self.getValue()
        return other // self._value
    def __rmod__(self, other):
        self.getValue()
        return other % self._value
    def __rpow__(self, other):
        self.getValue()
        return other ** self._value
    def __iadd__(self, other):
        self.getValue()
        self._value += other
    def __isub__(self, other):
        self.getValue()
        self._value -= other
    def __imul__(self, other):
        self.getValue()
        self._value *= other
    def __itruediv__(self, other):
        self.getValue()
        self._value /= other
    def __ifloordiv__(self, other):
        self.getValue()
        self._value //= other
    def __imod__(self, other):
        self.getValue()
        self._value %= other
    def __ipow__(self, other):
        self.getValue()
        self._value **= other
    def __neg__(self):
        self.getValue()
        return -self._value
    def __pos__(self):
        self.getValue()
        return +self._value
    def __abs__(self):
        self.getValue()
        return abs(self._value)
    def __int__(self):
        self.getValue()
        return int(self._value)
    def __float__(self):
        self.getValue()
        return float(self._value)
    def __complex__(self):
        self.getValue()
        return complex(self._value)
    def __bytes__(self):
        self.getValue()
        return bytes(self._value)
    def __bool__(self):
        self.getValue()
        return bool(self._value)
    def __len__(self):
        self.getValue()
        return len(self._value)
    def __getitem__(self, item):
        self.getValue()
        return self._value[item]
    def __setitem__(self, key, value):
        self.getValue()
        self._value[key] = value
    def __delitem__(self, key):
        self.getValue()
        del self._value[key]
    def __iter__(self):
        self.getValue()
        return iter(self._value)
    def __next__(self):
        self.getValue()
        return next(self._value)
    def __contains__(self, item):
        self.getValue()
        return item in self._value
    def __call__(self, *args, **kwargs):
        self.getValue()
        return self._value(*args, **kwargs)
    def __enter__(self):
        self.getValue()
        return self._value.__enter__()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.getValue()
        return self._value.__exit__(exc_type, exc_val, exc_tb)
    def __await__(self):
        self.getValue()
        return self._value.__await__()
    def __aiter__(self):
        self.getValue()
        return self._value.__aiter__()
    def __aenter__(self):
        self.getValue()
        return self._value.__aenter__()
    def __aexit__(self, exc_type, exc_val, exc_tb):
        self.getValue()
        return self._value.__aexit__(exc_type, exc_val, exc_tb)
    def __anext__(self):
        self.getValue()
        return self._value.__anext__()
    def __hash__(self):
        self.getValue()
        return hash(self._value)
    def __format__(self, format_spec):
        self.getValue()
        return format(self._value, format_spec)
    def __and__(self, other):
        self.getValue()
        return self._value and other
    def __or__(self, other):
        self.getValue()
        return self._value or other
    def __rand__(self, other):
        self.getValue()
        return other and self._value
    def __ror__(self, other):
        self.getValue()
        return other or self._value
    def __floor__(self):
        self.getValue()
        return self._value.__floor__()
    def __ceil__(self):
        self.getValue()
        return self._value.__ceil__()
    def __round__(self, n=None):
        self.getValue()
        return round(self, n)
    def __cmp__(self, other):
        self.getValue()
        return self._value.__cmp__(other)

def Lazy(f: F) -> F:
    def f_lazy(*args, **kwargs):
        def f0():
            return f(*args, **kwargs)
        return LazyData(f0)
    return f_lazy