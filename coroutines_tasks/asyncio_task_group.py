import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(2, 'Hello'))
        task2 = tg.create_task(say_after(4, 'world!'))

        
        