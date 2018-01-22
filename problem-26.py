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
    rec = {}
    d = 1
    i = 1
    '''
        Some self talk:
            Assumption is recurring digits are not more than 9 digits thats considering the fact that if any of digits 1 - 9 repeats same cycle repeats.
            Thus below algorithm proceeds as below

            for each recurringDigit:
                if recurringDigit is part of dictionary key:
                    return value against that digit
                else
                    for each keys in dictionary:
                        append this recurring digit to values against those keys
                    insert this new recurringDigit as key with value as recurringDigit

            Okay so this yeilds 81 as answer if this is correct I'll go ahead and cleanup, BUT ... I'll do this only if this is correct

    '''
    while True:
        d *= 10
        r = d%n
        recDigit =  (d-r)/n
        dKey = recDigit%10
        if dKey in rec.keys():
            return rec[dKey]
        else:
            for key in rec.keys():
                rec[key] = (rec[key]*10)+(dKey)

            rec[dKey] = dKey

def Solve():
    seqList = []
    for i in range(1,1000):
        seq = recurringSequence(i)
        if seq != 0:
            seqList.append(seq)

    seqList.sort()
    print seqList[len(seqList) - 1]

    return 0



start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))
