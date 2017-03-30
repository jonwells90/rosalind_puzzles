#!/usr/bin/env python3

import numpy as np
import sys

"""
Problem 12 - Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first # ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred #
divisors?
"""

def prime_sieve(n):
    primes = list(range(2, n+1))
    for i, val in enumerate(primes):
        if primes[i] == 0:
            continue
        else:
            j = i + val
            while j < len(primes):
                primes[j] = 0
                j += val
    primes = [p for p in primes if p]
    return primes

def prime_factors(n):
    factors = []
    curr = n
    for div in prime_sieve(int(n**0.5)):
        while curr%div == 0:
            factors.append(div)
            curr = curr/div
    if curr > 1:
        factors.append(curr)
    return factors

def numfactors(n):
    num = 1
    factors = prime_factors(n)
    for i in set(factors):
        num *= factors.count(i) + 1
    return num

def triangle_number_divisors(numdivs):
    index, curr = 0, 0
    factors, factormax = 0, 0
    while factors < numdivs:
        index += 1
        curr += index
        factors = numfactors(curr)
        if factors > factormax:
            print(index, curr, factors)
            factormax = factors

if __name__ == '__main__':
    triangle_number_divisors(int(sys.argv[1]))
