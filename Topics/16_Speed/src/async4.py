import asyncio
import time
import concurrent.futures
from os import getpid


def hold(n):
    pid = getpid()
    print(f'Running task number {n} on process {pid}')
    time.sleep(n)
    return n


async def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(hold, i) for i in range(1,5)}
        for future in concurrent.futures.as_completed(futures):
            data = future.result()
            print(data)


start = time.time()
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(main())
loop.run_until_complete(future)
print("Execution time: ", time.time() - start)
