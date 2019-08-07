#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

'''

import time
import sys
import math



def isTheOneWeAreLookingFor(s):
    primes = [ 2, 3, 5, 7, 11, 13, 17 ]
    i = 1
    for p in primes:
        n = int(''.join(map(str,s[i:i+3])))
        if n%p != 0:
            return False
        i += 1

    return True

def permutations(s, i, l):
    if len(s) == i:
        if s[5] != '5' or int(s[3])%2 != 0 :
            return
        if isTheOneWeAreLookingFor(s):
            n = int(''.join(map(str,s)))
            if n not in l:
                l.append(n)

    for j in range(i, len(s)):
        s[i],s[j] = s[j],s[i]
        permutations(s,i+1,l)
        s[i],s[j] = s[j],s[i]

def getPermutations(nums):
    l = list()
    permutations(nums, 0, l)
    return l

def Solve_Naive():
    num = ['1','2','3','4','5','6','7','8','9','0']
    p   = getPermutations(num)
    s = 0
    for n in p:
        s += n

    return s

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

