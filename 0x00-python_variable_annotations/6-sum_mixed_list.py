#!/usr/bin/env python3
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns their sum.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats to be summed.

    Returns:
        float: The sum of the input list.
    """
    result = sum(mxd_lst)
    return result

# Testing the function
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print(sum_mixed_list.__annotations__)
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))

