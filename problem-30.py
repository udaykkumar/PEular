#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44
    As 1 = 14 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


'''

import time
import sys
import math


def getDigitPower(d,p):
    s = 0
    r = 0
    while d:
        r = d%10
        s += math.pow(r,p)
        d /= 10

    return s


def Solve_Naive():
    i = 10
    naiveSum = 0
    while i <= 204979:
        if i == getDigitPower(i,5):
            naiveSum += i
        i += 1
    return naiveSum

def Solve():
    return Solve_Naive()


start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

