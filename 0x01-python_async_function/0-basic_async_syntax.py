#!/usr/bin/env python3
"""synchronous coroutine that takes in an integer argumet named wait_random 
that waits for a random delay between 0 and max_delay seconds and eventually re
turns it"""
import asyncio
import random

async def wait_random(max_delay=10) -> float:
    """asyc coroutine"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
