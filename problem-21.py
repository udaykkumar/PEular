#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a !≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''

import time
import math
import sys


def sumOfPropDivs(n):
    sqRtN = int(math.sqrt(n))
    sumDivs = 0
    for i in range(2,sqRtN):
        if n%i == 0:
            if n/i == i :
                sumDivs += i
            else:
                sumDivs += i + n/i

    return (sumDivs + 1)


def getKey(x,y):
    if x > y:
        return str(x)+"-"+str(y)
    else:
        return str(y)+"-"+str(x)

dAmicParis = {}
def Solve():
    sumOfAmicableNos = 0
    for a in range(1,10001):
        d_a = sumOfPropDivs(a)
        d_b = sumOfPropDivs(d_a)
        if a == d_b :
            k = getKey( d_a, d_b )
            if k in dAmicParis:
                v = dAmicParis[k]
                sumOfAmicableNos += v[0] + v[1]
            else:
                v = [ d_a, d_b ]
                dAmicParis[k] = v
    return sumOfAmicableNos

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))
