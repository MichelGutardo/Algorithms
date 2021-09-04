#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primality' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

# >>> My answer
def primality(n):
    
    if(n%2 == 0 and  n!=2 or n==1 ): return "Not prime"

    for idx in range(3,int(math.sqrt(n)+1),2):
        if n % idx == 0:
            return "Not prime"
    return "Prime"
    
        
#Input HackerRank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
