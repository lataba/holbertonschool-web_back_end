#!/usr/bin/env python3
"""
Module for task 0-async_generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator that yields a random number between 0 and 10 every second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
