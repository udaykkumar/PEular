#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''

import time
import math
import sys
import string

def sumOfPropDivs(n):
    sqRtN = int(math.sqrt(n))
    sqRtN += 1
    sumDivs = 0
    for i in range(2,sqRtN):
        if n%i == 0:
            if n/i == i :
                sumDivs += i
            else:
                sumDivs += i + n/i
    return (sumDivs + 1)


def abundantNos(x):
    abDict = {}
    for n in range(1,x):
        propDivs = sumOfPropDivs(n)
        if propDivs > n:
            abDict[n] = 1
    return abDict

def Solve(x):
    x += 1
    d = abundantNos(x)
    abnos = d.keys()
    sumNos = 0
    for i in range(1,x):
        canBeExpressedAsSum = False
        for n in abnos:
            n1 = i - n
            if n1 > 0:
                if n1 in d: # Check in dictionary not in list,
                    canBeExpressedAsSum = True
                    break
        if not canBeExpressedAsSum:
            sumNos += i

    return sumNos

start_time = time.time()
print Solve(28123)
print("--- %s seconds ---" % (time.time() - start_time))
