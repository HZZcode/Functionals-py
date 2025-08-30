from typing import Iterable, Generator


def product_dict[TKey, TValue](_dict: dict[TKey, Iterable[TValue]]) -> Generator[dict[TKey, TValue], None, None]:
    if len(_dict) == 0:
        yield dict()
        return
    keys: list[TKey] = list(_dict.keys())
    first_key: TKey = keys[0]
    first_values: TValue = _dict[first_key]
    remaining: dict[TKey, Iterable[TValue]] = {key: _dict[key] for key in keys[1:]}
    for first_value in first_values:
        for sub_product in product_dict(remaining):
            yield {first_key: first_value, **sub_product}
