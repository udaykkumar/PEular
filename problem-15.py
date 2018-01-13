#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

Some Math:
    Wiki - says
        "The number of lattice paths from {\displaystyle (0,0)} (0,0) to {\displaystyle (n,k)} (n,k) is equal to the binomial coefficient {\displaystyle {\binom {n+k}{n}}} {\binom  {n+k}{n}}"


'''

import time
import sys


def factorial(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact

def getBionomialCoefficient(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def getNoLatticepaths(n,k): # from (0,0) to (n,k)
    return getBionomialCoefficient(n+k,k)

start_time = time.time()
print getNoLatticepaths(20,20)
print("--- %s seconds ---" % (time.time() - start_time))
