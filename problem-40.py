#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''

import time
import sys
import math


def Solve_Naive():
    d = '0'
    for i in range(1,100000):
            d += str(i)
    j = 10
    m = 1
    while j < 1000000:
        m *= int(d[j])
        j *= 10

    return m

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

