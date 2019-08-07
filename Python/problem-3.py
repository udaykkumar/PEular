#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?

'''

import time
import math

def isFactor(x,y):
    if x%y == 0:
        return True
    return False


def largestPrimeFactor_Naive_Solution(n):
    largefactor = 1
    factor  = 2
    while (n > 1):
        if isFactor(n,factor) :
            n /= factor
            if factor > largefactor:
                largefactor = factor
        else:
            factor += 1
    return largefactor

start_time = time.time()
print largestPrimeFactor_Naive_Solution(600851475143)
print("--- %s seconds ---" % (time.time() - start_time))

