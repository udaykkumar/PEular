#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

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
    s = 0
    MAX = 9999
    for i in range( 1, MAX):
        si = 0
        ss = ""
        for n in range( 1, 50):
            ss += str(n*i)
            if len(ss) == 9:
                si = int(ss)
                if isPandigital(si):
                   if si > s:
                       s = si
    return s

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

