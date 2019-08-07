#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''

import time
import sys
import math


def hasEvenDigit(n):
    if n == 2:
        return False

    while n > 0:
        r = n%10
        if r%2 == 0:
            return True
        n /= 10

    return False

def getPrimesWithoutAfactorEvenDigit(n):
    p = []
    seive = [True]*(n+1)
    for i in range(2,n+1):
        if seive[i] == False:
            continue
        if not hasEvenDigit(i):
            p.append(i)


        for j in range(i+i, n, i):
            seive[j] = False
    return p


def rotateOnce(n,d):
    p = [1, 1, 10, 100, 1000, 10000, 100000 ]
    r = n%10
    n = n/10
    ret =  (r * p[d]) + n
    return ret

def isCirularPrime(n, primes):
    p = n
    nLen = 0

    while n > 0:
        nLen += 1
        n /= 10

    n = p
    n = rotateOnce(n, nLen)

    while n != p:
        if n not in primes:
            return False
        n = rotateOnce(n, nLen)

    return True

def Solve_Naive():
    n = 0
    primes = getPrimesWithoutAfactorEvenDigit(1000000)
    for p in primes:
        if isCirularPrime(p, primes):
            n += 1
    return n

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

