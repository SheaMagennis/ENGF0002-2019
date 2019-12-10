import time
from ctypes import *
libprimes = CDLL("./libprimes.so")
 
#call C function to check connection
start = time.time()
count = libprimes.countprimes() 
end = time.time()
 
print("counted ", count, "primes in", end - start, "seconds")
