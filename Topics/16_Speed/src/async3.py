import asyncio
import sys
import time
from os import getpid

async def hold(sec):
    pid = getpid()
    print(f'Running for {sec} seconds on process {pid}')
    await asyncio.sleep(sec)

async def main():
    print("in main")
    tasks = []

    for seconds in [2, 3, 4]:
        task = asyncio.ensure_future(hold(seconds))
        tasks.append(task)

    await asyncio.gather(*tasks)
    print("main done")

start = time.time()
loop = asyncio.get_event_loop()
print("setting up tasks...")
future = asyncio.ensure_future(main())
print("setup done.")
loop.run_until_complete(future)
print("Execution time:", time.time() - start)
