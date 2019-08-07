#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Euler discovered the remarkable quadratic formula:

    n2+n+41
    n2+n+41
    It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39. However, when n=40,402+40+41=40(40+1)+41n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41n=41,412+41+41 is clearly divisible by 41.

    The incredible formula n2−79n+1601n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

        n2+an+b
        n2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

        where |n||n| is the modulus/absolute value of nn
        e.g. |11|=11|11|=11 and |−4|=4|−4|=4
        Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0n=0.

'''

import time
import sys

SEIVE_SIZE = 100000
seive = [True]*(SEIVE_SIZE)

def getPrimes(n):
    primes = []
    k = 10
    for i in range(2,SEIVE_SIZE):
        if not seive[i] :
            continue

        if i <= n:
            primes.append(i)
            primes.append(i*(-1))

        for j in range( i+i, SEIVE_SIZE, i ):
            seive[j] = False

    return primes

def Solve():
    primes_b = getPrimes(1000)
    maxN = 0
    maxA = 0
    maxB = 0
    for b in primes_b:
        for a in range(-1000, 1001 ):
            for n in range( 0, 1000 ):
                p = (n*n) + (a)*(n) + b
                if not seive[abs(p)]:
                    break
                n += 1
            if maxN < n:
                maxN = n
                maxA = a
                maxB = b

    return (maxA * maxB)


start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

