#!/usr/bin/env python3
"""
Module for measuring runtime of async_comprehension.
"""

import asyncio
from time import time
from async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel using asyncio.gather
    and measures the total runtime.

    Returns:
    - float: Total runtime.
    """
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time()

    return end_time - start_time

