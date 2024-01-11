#!/usr/bin/env python3
def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The concatenated string of str1 and str2.
    """
    result = str1 + str2
    return result

# Testing the function
str1 = "egg"
str2 = "shell"
print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)

