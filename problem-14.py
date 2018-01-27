#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
        It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

        Which starting number, under one million, produces the longest chain?

        NOTE: Once the chain starts the terms are allowed to go above one million.

'''

import time
import sys

def getChain(n):
    chain = 0
    while ( n > 1 ):
        chain += 1
        if n%2 == 0:
            n /= 2
        else:
            n = (3*n) +1
        chain += 1
    return chain

chainCache = {}

def getChainImproved(n):
    if n <= 1 :
        return 0

    if n in chainCache:
        return chainCache[n]

    chain = 0
    if n%2 == 0:
        chain = (getChainImproved(n/2) +1)
    else:
        chain = (getChainImproved((3*n)+1) +1)

    chainCache[n] = chain
    return chain


#TODO This needs improvement
def startingNumberWithLongestChain_Naive_BruteForce():
    cLen = 0
    cGen = 0
    for n in range(1000005):
        chain = getChain(n)
        if cLen < chain:
            cLen = chain
            cGen = n
    return cGen

#TODO This first attempt towards improvement
def startingNumberWithLongestChain_Improvement_Trial():
    cLen = 0
    cGen = 0
    for n in range(1000005):
        chain = getChainImproved(n)
        if cLen < chain:
            cLen = chain
            cGen = n
    return cGen

start_time = time.time()
print startingNumberWithLongestChain_Naive_BruteForce()
print("--- startingNumberWithLongestChain_Naive_BruteForce  %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print startingNumberWithLongestChain_Improvement_Trial()
print("--- startingNumberWithLongestChain_Improvement_Trial %s seconds ---" % (time.time() - start_time))
