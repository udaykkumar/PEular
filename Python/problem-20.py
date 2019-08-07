#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''

import time
import sys


def getFact(n):
    fact = 1
    while (n>0):
        fact *= n
        n -= 1
    return fact

def Solve():
    res  = 0
    fact = getFact(100)
    while fact > 0 :
        res += fact%10
        fact //= 10
    return res

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))
