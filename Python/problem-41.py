#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''

import time
import sys
import math



def isPandigital(n):
    pans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n > 0:
        r = n%10
        if r == 0:
            return False

        if pans[r] > 0:
            return False

        pans[r] = 1
        n /= 10

    return True

def _permute(s, i, l):
    if s[len(s)-1]%2 == 0 or s[len(s)-1] == 5:
        return

    if i == len(s):
        n = int(''.join(map(str,s)))
        l.append(n)

    for j in range(i,len(s)):
        s[i],s[j] = s[j],s[i]
        _permute(s,i+1,l)
        s[i],s[j] = s[j],s[i]


def toArray(n):
    l = []
    while n > 0 :
        l.append(n%10)
        n /= 10
    return l

def permute(n):
    s = toArray(n)
    l = list()
    _permute(s,0, l)
    return l


def isPrime(n, primes ):
    sqN = int(math.sqrt(n))+1
    for i in primes:
        if i > sqN:
            break
        if n%i == 0:
            return False

    return True

def Solve_Naive():
    num=123456789
    maxPrimes = 102690
    primes = []
    seive = [True] * maxPrimes # Max Permutations of 123456789
    for i in range(2, maxPrimes):
        if seive[i] == False:
            continue
        primes.append(i)
        for j in range(i+i, maxPrimes, maxPrimes):
            seive[j] = False

    while num > 0:
        permutations = permute(num)
        permutations.sort()
        for n in reversed(permutations):
            if isPrime(n, primes):
                return n
        num /= 10

    return 0

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

