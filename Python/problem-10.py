#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

import time


def getPrimesSum(n):
    primesSum = 0
    seive = [True] * (n+1)
    for i in range( 2, n+1 ):
        if seive[i] == False:
            continue
        primesSum += i
        for j in range(i+i, n+1, i):
            seive[j] = False
    return primesSum


def PrimesSum(n):
    return getPrimesSum(n)


start_time = time.time()
print PrimesSum(2000000)
print("--- %s seconds ---" % (time.time() - start_time))
