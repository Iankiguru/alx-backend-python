import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns an asyncio.Task.
    :param max_delay: The maximum delay for wait_random.
    :return: asyncio.Task for wait_random with the specified max_delay.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task

# Test case
async def test(max_delay: int) -> None:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

