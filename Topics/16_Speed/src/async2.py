import asyncio
from os import getpid

async def hold(seconds):
    pid = getpid()
    print(f'Waiting {seconds} seconds on process {pid}...')
    await asyncio.sleep(seconds)
    print(f'Done waiting {seconds} seconds.')

async def main():
    await asyncio.gather(
        hold(1),
        hold(2),
        hold(3),
    )

asyncio.run(main())
