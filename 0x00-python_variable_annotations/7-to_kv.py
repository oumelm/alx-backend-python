#!/usr/bin/env python3


'''a module that takes two arguments and returns a tuple'''


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''A function that retuns a tuple'''

    return (k, v**2)
