from typing import TypeVar

T = TypeVar('T')

def NotNone(t: T | None) -> T:
    assert t is not None, 'NotNone Check Failed'
    return t