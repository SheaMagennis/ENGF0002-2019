#include<stdio.h>
#include<stdbool.h>

#define MAXPRIME 100000  /* ugly upper bound */

int countprimes() {
  int primes[MAXPRIME];
  int primecount = 0;
  for (int i = 2; i < 100000; i++) {
    int is_prime = true;
    for (int index = 0; index < primecount; index++) {
      if (i % primes[index] == 0) {
	is_prime = false;
	break;
      }
    }
    if (is_prime) {
      primes[primecount++] = i;
    }
  }
  return primecount;
}

int main() {
  printf("found %d primes", countprimes());
}
