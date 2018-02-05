#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

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


def Solve_Naive():
    l = []
    s = 0
    for mr in range(1,100):
        if not isPandigital(mr):
            continue
        for md in range(100,100001):
            if isPandigital(md):
                prod = md * mr
                if isPandigital(prod):
                    nstr = str(mr)+str(md)+str(prod)
                    if len(nstr) > 9:
                        break
                    if len(nstr) == 9:
                        if isPandigital(int(nstr)):
                            if prod not in l:
                                l.append(prod)
                                s += prod
    return s

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

