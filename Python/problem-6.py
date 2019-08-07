#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

import time

def sumSquaresOfNNaturalNos(n):
    return n * (n + 1) * (2*n + 1) / 6

def sumOfNNaturalNos(n):
    return n * (n + 1) / 2


def difference(n):
    s1 = sumSquaresOfNNaturalNos(n)
    s2 = sumOfNNaturalNos(n)
    return ( ( s2 * s2 ) - s1 )

start_time = time.time()
print difference(100 )
print("--- %s seconds ---" % (time.time() - start_time))
