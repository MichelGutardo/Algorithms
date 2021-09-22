#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

#>>>  My answer
def alternatingCharacters(s):
    size = len(s)
    if(size <=1 ):
        return 0
    idx=0 
    count =0
    while idx < size-1:
        if(s[idx] == s[idx+1]):
            count+=1 
        idx+=1
    return count
    

#Input HR
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
