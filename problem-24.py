#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''

import time
import sys
import itertools



def permute(s, i, n):
    if i == n:
        print s

    for j in range(i,n):
        s[i],s[j] = s[j],s[i]
        permute(s, i+1, n)
        s[i],s[j] = s[j],s[i]


#This is really a cheat and not definately not how this is supposed to be
# I'll have to revisit this TODO
def getNthLexicographicPermutation(s,n):
    permutations = list(itertools.permutations(s));
    return ''.join(permutations[n-1])

def Solve(s,n):
    return getNthLexicographicPermutation(s,n)

start_time = time.time()
print Solve(list("0123456789"),1000000)
print("--- %s seconds ---" % (time.time() - start_time))
