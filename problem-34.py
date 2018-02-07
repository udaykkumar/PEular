#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import time
import sys
import math

def getFactorial(n):
    if n == 0:
        return 1

    f = 1
    while n > 0:
        f *= n
        n -= 1

    return f

def Solve_Naive():
    n = 10
    s = 0
    while n < 100000:
        fN = n
        fDigitsOfN = 0
        while fN > 0:
            fDigitsOfN += getFactorial(fN%10)
            fN /= 10

        if n == fDigitsOfN:
            s += n

        n += 1

    return s

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

