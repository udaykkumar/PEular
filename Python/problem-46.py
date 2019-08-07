#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''

import time
import sys
import math


def getPrimes(n):
    seive = [True] * (n+1)
    primes = []
    for i in range(2, n+1):
        if seive[i] == False:
            continue
        primes.append(i)
        for j in range(i+i, n+1, i):
            seive[j] = False

    return primes


def Solve_Naive():
    res = 0
    MAX = 10000
    primes = getPrimes(MAX)
    n = 3
    while n < MAX:
        if n not in primes:
            SatisfiesTheRule = False
            SqRt = 0
            for p in primes:
                if n < p:
                    break
                lhs = int( (n-p)/2 )
                SqRt = int(math.sqrt(lhs))
                if SqRt*SqRt == lhs:
                    SatisfiesTheRule = True
                    break
            if SatisfiesTheRule == False:
                return n
        n += 2

    return res

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

