#!/usr/bin/env python3
"""
Module for task 4-tasks.py
"""

from typing import List
from heapq import heappush

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine called task_wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random n times
    with the specified max_delay.
    """
    delay_list: List[float] = []
    delay: float = 0
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        heappush(delay_list, delay)
    return delay_list
