#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

import time


def ifAtleastOneElementIsDivisible(l,n):
    if n == 1:
        return False

    atLeastAnElementIsDivisible = False
    for index, item in enumerate(l):
        if item%n == 0:
            l[index] = item/n
            atLeastAnElementIsDivisible = True
    return atLeastAnElementIsDivisible


def lcm( mylist ):
    lcm     = 1
    for i in xrange(2,21):
        while ( ifAtleastOneElementIsDivisible(mylist,i) ):
            lcm *= i
    return lcm



start_time = time.time()
mylist     = list(xrange(1,21))
print lcm( mylist )
print("--- %s seconds ---" % (time.time() - start_time))

