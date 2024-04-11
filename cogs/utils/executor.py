#From sir-lancebot

import asyncio
from concurrent.futures import ThreadPoolExecutor

_EXECUTOR = ThreadPoolExecutor(10)

async def in_executor(func, *args):
    """
    Runs the given synchronous function `func` in an executor.
    This is useful for running slow, blocking code within async
    functions, so that they don't block the bot.
    """

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(_EXECUTOR, func, *args)