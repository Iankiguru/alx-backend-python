#!/usr/bin/env python3
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v and returns a tuple.

    Args:
        k (str): The string element of the tuple.
        v (Union[int, float]): The int or float element of the tuple.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of the int or float v (annotated as a float).
    """
    result = (k, v ** 2)
    return result

# Testing the function
print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))

