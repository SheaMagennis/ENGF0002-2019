import time
primes = []
start = time.time()
for i in range(100000):
    primes.append(0)
init = time.time()
print("init took", init - start, "seconds")
primecount = 0
for i in range(2,100000):
    is_prime = True
    for index in range(0, primecount):
        if i%primes[index] == 0:
            is_prime = False
            break
    if is_prime:
        primes[primecount] = i
        primecount += 1
print("Found ", len(primes), "primes")
print("search took", time.time() - init, "seconds")
