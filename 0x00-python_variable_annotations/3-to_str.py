#!/usr/bin/env python3
def to_str(n: float) -> str:
    """
    Returns the string representation of a floating-point number.

    Args:
        n (float): The input floating-point number.

    Returns:
        str: The string representation of the input number.
    """
    result = str(n)
    return result

# Testing the function
pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))

