#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23


NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

'''

import time
import sys
import numpy as np  # Deal with the matrix

def getMatrix(coOrdinates):
    foo    =    [ str(line).strip('\r\n').lstrip(' ').rstrip(' ').split(' ') for line in sys.stdin ]
    grid   =    [ max(int,x) for x in foo ]
    m    =  len(foo)
    n    =  len(foo[m-1])

    matrix =    [[0 for x in range(m)] for y in range(n)]
    for x in range(m):
        for y in range(n):
            if y <= x :
                matrix[x][y] = int(foo[x][y])

    coOrdinates[0] = m
    coOrdinates[1] = n
    return matrix


def max(x, y):
    if x > y :
        return x
    else:
        return y

def createKey(i,j):
    return str(i)+"-"+str(j)

rDict = {}

def maxRoutes(matrix,i,j,m,n):
    # Boundary Conditions
    if (i >= m) or (j >= n):
        return 0

    # if already calculated for this
    # return from here, don't recurse
    key = createKey(i,j)
    if key in rDict:
        return rDict[key]

    # recurse and calculate more
    maxRoute =  matrix[i][j] + max( maxRoutes( matrix, i+1, j, m, n), maxRoutes( matrix, i+1, j+1, m, n) )

    # Update dictionary so we don't do the same mistake again
    if maxRoute not in rDict:
        rDict[key] = maxRoute

    return maxRoute


def Solve():
    coOrdinates = [0]*2
    matrix =  getMatrix(coOrdinates)
    return maxRoutes(matrix,0,0,coOrdinates[0],coOrdinates[1])

start_time = time.time()
print Solve()
print("--- %s seconds ---" % (time.time() - start_time))
