def NotNone[T](t: T | None) -> T:
    assert t is not None, 'NotNone Check Failed'
    return t
