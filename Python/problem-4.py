#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

import time

def isPallindrom(n):
    strn = str(n)
    if strn == strn[::-1]:
        return True
    return False

def isLargestPallindromProduct(n):
    for x in range( 999, 100, -1 ):
        if n%x == 0:
            factor2 = n/x
            if factor2 > 99 and factor2 < 1000:
                return True
    return False

def getLargestPallindromProduct(max):
    for i in range ( max, 100000, -1 ):
        if isPallindrom(i):
            if isLargestPallindromProduct(i):
                return i


start_time = time.time()
print getLargestPallindromProduct( max = (999*999) )
print("--- %s seconds ---" % (time.time() - start_time))

