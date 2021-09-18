#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

#>>> My Answer
def sockMerchant(n, ar):
    
    count = 0
    idx2 = 0
    idx = 0
    found = False
    size = len(ar)
    
    while idx < size:
        idx2 = idx +1 
        found = False
        
        while idx2 < size:
            
            if(ar[idx2]== ar[idx]):
                del ar[idx2]
                del ar[idx]
                size=len(ar)
                count+=1
                idx=0
                found=True
                break
            idx2+=1
        if(found is not True):
            idx+=1  
                    
    return count 
        
# Input HackerRank    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
