#!/usr/bin/env python3
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats and returns their sum.

    Args:
        input_list (List[float]): The list of floats to be summed.

    Returns:
        float: The sum of the input list.
    """
    result = sum(input_list)
    return result

# Testing the function
floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))

