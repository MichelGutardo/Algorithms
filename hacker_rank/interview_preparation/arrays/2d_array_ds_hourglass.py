#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#>>> My Answer
def hourglassSum(arr):
    
    if(len(arr)<3):
        return 0
    
    limit_col = len(arr[0])-2
    limit_row = len(arr) - 2
    idx_col =0
    idx_row =0
    sum_hourglass = []
    total_current = 0
        
    while idx_col < limit_col:
        
        #sum first line
        total_current += arr[idx_row][idx_col]
        total_current += arr[idx_row][idx_col+1]
        total_current += arr[idx_row][idx_col+2]
           
        #sum middle
        total_current += arr[idx_row+1][idx_col+1]
            
        #sum third line
        total_current += arr[idx_row+2][idx_col]
        total_current += arr[idx_row+2][idx_col+1]
        total_current += arr[idx_row+2][idx_col+2]
            
        sum_hourglass.append(total_current)
        total_current = 0
            
        idx_col += 1
        
        #back first column hourglass in next line
        if(idx_col == limit_col):
            idx_row+=1
            idx_col =0
            
            if(idx_row == limit_row):
                break
    
    return max(sum_hourglass)
            
        
#Hacker Rank Input
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
