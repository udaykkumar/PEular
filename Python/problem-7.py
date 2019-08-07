#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

'''

import time

def createSeive(n):
    primesList = []
    seive = [True] * (n+1)
    for i in range( 2, n+1 ):
        if seive[i] == False:
            continue
        primesList.append(i)
        for j in range(i+i, n+1, i):
            seive[j] = False
    return primesList



start_time = time.time()
primes =  createSeive(1000000)
print primes[10000]
print("--- %s seconds ---" % (time.time() - start_time))
