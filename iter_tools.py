#!/usr/bin/env python3.5
from pprint import pprint as pp
from itertools import islice, count, chain
import math


def isPrime(num):
    # Returns True if num is a prime number, otherwise False.
    # Note: Generally, isPrime() is slower than primeSieve().
    # all numbers less than 2 are not prime
    if num < 2:
        return False

    # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# itertools: functions for creating iterators for efficient looping
#       - islice: provides lazy slicing like list slice [:]

# sum of first 1000 primes
# count() open ended version of range (don't have to specify an end boundary)
# hence: prime generator = (x for x in count() if isPrime(x))
#        islice( prime_generator, 1000)

# setup the "prime generator"
prime_generator = (x for x in count() if isPrime(x))

# take a slice of 1000 from the prime_generator
k_primes = islice(prime_generator, 1000)
pp(k_primes)  # << This is an itertools.islice object
# sum forces calc of 1k primes
print("sum(k_primes) = ", sum(k_primes))

# this can also be written as
# print("sum(x_primes) = ", sum(x_primes))
print("sum(x_primes) = ", sum(islice((x for x in count() if isPrime(x)), 1000)))


# any / all: same as logical operators and / or:  for iterable series of Bool
# any returns True if any in series are True
#       any([Flase, False, True])
# all returns True if all in series are True
#       all([Flase, False, True])
print("any([False, False, True]) = ", any([False, False, True]))
print("all([False, False, True]) = ", all([False, False, True]))

# use any with a generator

print("any(isPrime(x) for x in range(1328, 1361)) = ",
      any(isPrime(x) for x in range(1328, 1361)))

print("all(name == name.title() for name in ['London', 'New York', 'Sydney']) = ",
      all(name == name.title() for name in ['London', 'New York', 'Sydney']))

# zip:  sycnhronize items over two iterable series
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for item in zip(odds, evens, zeros):
    print(item)

for od, ev, zilch in zip(odds, evens, zeros):
    print("even # = {}   odd # = {} zilch={}".format(ev, od, zilch))

# chain:  chain iterable series together
nums = chain(odds, evens, zeros)
print("all( n>= 0 for n in nums) = ", all(n >= 0 for n in nums))
