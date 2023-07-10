#!/usr/bin/env python3
"""function task_wait_random that takes an integer max_delay and returns a 
asyncio"""
import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task
