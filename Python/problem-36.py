#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

'''

import time
import sys
import math

def Base2(n):
    l = []
    while n > 0:
        l.append(n&0x01)
        n >>= 1
    return l[::-1]

def isPallindrom(s):
    if s == s[::-1]:
        return True
    return False

def Solve_Naive():
    s = 0
    n = 1
    for n in range(1,1000000):
        if isPallindrom(str(n)):
            if isPallindrom( Base2(n) ) :
                s += n
    return s

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

