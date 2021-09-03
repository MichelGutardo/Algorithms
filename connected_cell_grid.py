#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#


# >>> My answer
def maxRegion(grid):
    
    visited=[0]
    idxR= 0
    idxC= 0
    count=0
    max_rows = len(grid)
    max_column = len(grid[0])
    while idxR < max_rows:
        while idxC < max_column:
            if grid[idxR][idxC] ==1:
                visited.append(dfs(grid,idxR,idxC))
            idxC+=1                
        idxR+=1
        idxC=0
    return max(visited)
            
    
def dfs(grid,idxR,idxC,count=0):
    count+=1
    grid[idxR][idxC]=0
    count+=  checkUp(grid,idxR,idxC) 
    count+=checkUpRight(grid,idxR,idxC)     
    count+=checkUpLeft(grid,idxR,idxC)     
    count+=checkDown(grid,idxR,idxC)     
    count+=checkDownRight(grid,idxR,idxC)     
    count+=checkDownLeft(grid,idxR,idxC)     
    count+=checkRight(grid,idxR,idxC)     
    count+=checkLeft(grid,idxR,idxC)     
    return count
    
def checkUp(grid,idxR,idxC):
    if (idxR-1) >=0 :
        if grid[idxR-1][idxC]==1:
            return dfs(grid,idxR-1,idxC)
    return 0
def checkDown(grid,idxR,idxC):
    if (idxR+1) <  len(grid):
        if grid[idxR+1][idxC]==1:
           return dfs(grid,idxR+1,idxC)                 
    return 0
def checkLeft(grid,idxR,idxC):
    if (idxC-1) >=0:
        if grid[idxR][idxC-1]==1:
            return dfs(grid,idxR,idxC-1)
    return 0
def checkRight(grid,idxR,idxC):
    if ( idxC+1) < len(grid[idxR])  :
        if grid[idxR][idxC+1]==1:
            return dfs(grid,idxR,idxC+1)
    return 0
def checkUpRight(grid,idxR,idxC):
    if (idxR-1) >= 0 :
        if (idxC+1) < len(grid[0]) :
            if grid[idxR-1][idxC+1]==1:
                return dfs(grid,idxR-1,idxC+1)
    return 0
def checkUpLeft(grid,idxR,idxC):
    if (idxR-1) >= 0 :
        if (idxC-1) >= 0 :
            if grid[idxR-1][idxC-1]==1:
               return dfs(grid,idxR-1,idxC-1)
    return 0

def checkDownRight(grid,idxR,idxC):
    if (idxR+1) < len(grid):
        if (idxC+1) < len(grid[0]) :
            if grid[idxR+1][idxC+1]==1:
                return dfs(grid,idxR+1,idxC+1)    
    return 0
def checkDownLeft(grid,idxR,idxC):
    if (idxR+1) < len(grid) :
        if (idxC-1) >= 0 :
            if grid[idxR+1][idxC-1]==1:
               return dfs(grid,idxR+1,idxC-1)
    return 0


#Input HackerRank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
