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



def Solve(sd):
    maxRecurringLen  = 0
    for d in range(sd-1, 0, -1):
        if maxRecurringLen > d:
            break

        remaindersPosition = [0]*(d+1)
        value = 1
        pos   = 0

        while remaindersPosition[value] == 0 and value != 0 :
            remaindersPosition[value] = pos
            value *= 10
            value %= d
            pos   += 1

        if pos - remaindersPosition[value] > maxRecurringLen:
            maxRecurringLen = pos - remaindersPosition[value]

    return maxRecurringLen



start_time = time.time()
print Solve(1000)
print("--- %s seconds ---" % (time.time() - start_time))

