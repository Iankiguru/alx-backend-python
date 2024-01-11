#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function that multiplies a float by the multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    
    return multiplier_function

# Testing the function
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))

