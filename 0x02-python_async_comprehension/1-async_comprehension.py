#!/usr/bin/env python3
"""
Module for asynchronous comprehension.
"""

from typing import List
from async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using asynchronous comprehension over async_generator.

    Returns:
    - List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]

