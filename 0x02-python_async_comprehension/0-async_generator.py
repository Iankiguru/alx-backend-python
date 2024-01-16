#!/usr/bin/env python3
"""
Module for asynchronous generator.
"""

import asyncio
import random

async def async_generator() -> float:
    """
    Coroutine that yields a random number between 0 and 10 after waiting for 1 second.

    Returns:
    - float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

