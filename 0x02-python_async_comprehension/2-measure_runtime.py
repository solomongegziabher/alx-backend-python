#!/usr/bin/env python3
"""
Runtime for four parallel comprehensions
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return total runtime"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = time.perf_counter() - start
    return end
