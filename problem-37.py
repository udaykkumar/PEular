#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''

import time
import sys
import math


def getLen(n):
    l = 0
    while n > 0:
        l += 1
        n /= 10
    return l

def getPrimes():
    p = {}
    MAX = 1000000
    seive = [True] * MAX
    for i in range(2, MAX):

        if seive[i] == False:
            continue

        p[i] = getLen(i)

        for j in range(i+i, MAX, i):
            seive[j] = False

    return p


def isTrunCataBasePrimeFromLeft(n, p):
    ret = True
    while n > 0 :
        if n not in p:
            ret =  False
            break
        n /= 10
    return ret


def isTrunCataBasePrimeFromRight(n, p):
    d = [1, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000 ]
    ret = True
    while n > 0 :
        if n not in p:
            ret = False
            break
        n = n - n/d[p[n]]*d[p[n]]

    return ret


def Solve_Naive():
    s = 0
    primes = getPrimes()
    for p in primes:
        if p < 10:
            continue
        if isTrunCataBasePrimeFromLeft(p, primes):
            if isTrunCataBasePrimeFromRight(p, primes):
                s += p

    return s

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

