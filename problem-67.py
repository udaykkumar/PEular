#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)



'''

import time
import sys

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
