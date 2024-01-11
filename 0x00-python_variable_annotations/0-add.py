#!/usr/bin/env python3
def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers and returns their sum.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        float: The sum of the two input numbers.
    """
    result = a + b
    return result

# Testing the function
print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

