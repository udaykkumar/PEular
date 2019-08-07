#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The nth term of the sequence of triangle numbers is given by, tn = $n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

'''

import time
import sys
import math



def getWordValue(word):
    d = { 'A' : 1,  'B' : 2,  'C' : 3,  'D' : 4,  'E' : 5,  'F' : 6,  'G' : 7,
          'H' : 8,  'I' : 9,  'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14,
          'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21,
          'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26 }
    v = 0
    for l in word:
        v += d[l]

    return v

def Solve_Naive():
    triangleNos = { }
    for x in range(1, 100):
        n = x * (x + 1) / 2
        triangleNos[n] = x

    totalWords = 0
    for line in sys.stdin:
        words =  line.split(",")
        for w in words:
            w = w.rstrip('"').lstrip('"')
            wordValue = getWordValue(w);
            if wordValue in triangleNos:
                totalWords += 1

    return totalWords

def Solve():
    return Solve_Naive()

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))

