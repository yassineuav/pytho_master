import asyncio

async def main():
    print('hello')
    await asyncio.sleep(5)
    print('hello world')

asyncio.run(main())
