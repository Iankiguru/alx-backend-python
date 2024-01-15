import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with the specified max_delay.
    :param n: The number of times to spawn task_wait_random.
    :param max_delay: The maximum delay for each task_wait_random call.
    :return: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # Gathering the results using asyncio.gather to run them concurrently
    results = await asyncio.gather(*tasks)
    # Sorting the results in ascending order
    sorted_delays = sorted(results)
    return sorted_delays

# Test case
n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

