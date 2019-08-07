#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import time
import sys
import math

def abc(pSum):
    sets = 0
    for a in range(1, pSum/3):
        for b in range(a+1, pSum/2, 1):
            c = pSum - a - b
            if a*a + b*b == c*c :
                #return a*b*c
                #print a, b, c
                sets += 1
    return sets

def Solve_Naive():
    maxset = 0
    maxP   = 0
    for p in range( 3, 1000, 3):
        sets = abc(p)
        if sets > 0:
            if sets > maxset:
                maxset = sets
                maxP   = p

    return maxP

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

