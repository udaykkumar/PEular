#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


'''

import time


def abc():
    pSum = 1000
    for a in range(1, pSum/3):
        for b in range(a+1, pSum/2, 1):
            c = pSum - a - b
            if a*a + b*b == c*c :
                return a*b*c


start_time = time.time()
print abc()
print("--- %s seconds ---" % (time.time() - start_time))
