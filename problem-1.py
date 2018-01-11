#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

import time

def getMultiplesSum(n):
    sum = 0
    for n in range(n):
        if n%3 == 0 or n%5 == 0 :
            sum += n

    return sum

start_time = time.time()
print getMultiplesSum(1000)
print("--- %s seconds ---" % (time.time() - start_time))


