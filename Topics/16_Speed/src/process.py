import time
from os import getpid
from multiprocessing import Process

def hold(sec):
    pid = getpid()
    print(f'Running for {sec} seconds in process {pid}')
    return time.sleep(sec)

start = time.time()
processes = []
for seconds in [2, 3, 4]:
    processes.append( Process(target=hold, args=(seconds,)) )

for process in processes:
    process.start()
    
for process in processes:
    process.join()

print("Execution time:", time.time() - start)

