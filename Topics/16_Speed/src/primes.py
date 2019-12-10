primes = []
for i in range(2,100000):
    is_prime = True
    for p in primes:
        if i%p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print("Found ", len(primes), "primes")
