#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
        How many different ways can £2 be made using any number of coins?

'''

import time
import sys
import math


c = [200, 100, 50, 20, 10, 5, 2, 1 ]

count = 0
def solve_recurse(p, r, i, n):
    global count
    if r == 0 or i == n :
        count += 1
        return

    for j in range( 0, (r/c[i]+1) ):
        solve_recurse( p, r - j * c[i], i+1, n )


def Solve_Naive(p):
     solve_recurse(p, 200, 0, len(c)-1)
     global count
     return count

def Solve(p):
    return Solve_Naive(p)


start_time = time.time()
print Solve(200)
print("--- %s seconds ---" % (time.time() - start_time))

