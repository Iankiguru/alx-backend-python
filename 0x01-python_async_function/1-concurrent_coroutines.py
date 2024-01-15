#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.
    :param n: The number of times to spawn wait_random.
    :param max_delay: The maximum delay for each wait_random call.
    :return: List of delays in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    # Gathering the results using asyncio.gather to run them concurrently
    results = await asyncio.gather(*delays)
    # Sorting the results in ascending order
    sorted_delays = sorted(results)
    return sorted_delays

# Test cases
print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

