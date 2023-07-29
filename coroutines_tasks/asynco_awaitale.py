import asyncio

async def nested():
    return 23

async def main():

    nested()

    print(await nested())

asyncio.run(main())