#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains an element from the input list and its length.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains an element and its length.
    """
    return [(i, len(i)) for i in lst]

