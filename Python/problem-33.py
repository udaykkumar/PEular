#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

import time
import sys
import math

def getPrimes(n):
    p = []
    s = [True]*(n+1)
    for i in range(2,n+1):
        if s[i] == False:
            continue
        p.append(i)
        for j in range(i+i, n+1, i):
            s[j] = False

    return p

def getPrimeFactors(x):
    pf = []
    s = int(math.sqrt(x))+1
    primes = getPrimes(s)
    for p in primes:
        while x%p == 0:
            pf.append(p)
            x /= p

    if x != 0:
        pf.append(x)

    return pf

def Solve_Naive():
    fractionDict = {}
    s = 0
    for i in range(1,100):
        if i%10 == 0:
            continue
        for j in range(i+1, 100):
            if j%10 == 0:
                continue
            fraction = float(i)/float(j)
            fractionDict.setdefault(fraction, []).append( i*100 + j)

    numerator = 1
    denominator = 1
    for k in fractionDict:
        for item in fractionDict[k]:
            n1 = (item/100)%10
            n2 = (item%100)/10
            n3 = item/1000
            n4 = item%10
            if n1 == n2:
                key = n3*100 + n4
                if key in fractionDict[k]:
                    numerator *= n3
                    denominator *= n4

    pfNumerator = getPrimeFactors(numerator)
    for p in pfNumerator:
        if denominator%p == 0:
            denominator /= p
            numerator /= p

    return denominator

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

