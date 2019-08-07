#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
 The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

 Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

import time
import sys
import math


def Solve_Naive():
    powerSum = 0
    for i in range(1,1001):
        powerSum += i**i

    return powerSum%10000000000


def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

