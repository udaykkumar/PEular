#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2=    0.5
    1/3=    0.(3)
    1/4=    0.25
    1/5=    0               .2
    1/6=    0.1(6)
    1/7=    0.(142857)
    1/8=    0.125
    1/9=    0.(1)
    1/10=   0.                  1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

import time
import sys


def recurringSequence(n):
    i = 0
    quotientList = []
    dividend = 1*10
    divisor  = n
    reminder = 1
    quotient = 1
    while ( i <= 100 and reminder != 0):
        while( dividend < divisor ):
            dividend *= 10
            quotientList.append('0')

        reminder = dividend%divisor

        quotient = (dividend-reminder)/divisor
        quotientList.append(str(quotient))

        dividend  = (reminder*10)
        i += 1

    if reminder == 0:
        return []
    return ''.join(quotientList)

def Solve(sd):
    largeSequenceGeneragedBy = 1
    for d in range(1,sd):
        rs = recurringSequence(d)
        #print "i = " , d , rs



start_time = time.time()
print Solve(1000)
print("--- %s seconds ---" % (time.time() - start_time))

