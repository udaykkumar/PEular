#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2 pow 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 pow 1000?
'''

import time
import sys


def getSumOfDigits(x,y):
    n = x**y
    s = 0
    while (n > 0):
        s += n%10
        n /= 10
    return s

start_time = time.time()
print getSumOfDigits(2,1000)
print("--- %s seconds ---" % (time.time() - start_time))
