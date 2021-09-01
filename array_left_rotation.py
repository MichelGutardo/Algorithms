#!/bin/python3

import collections
import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#


# >>> my answer 
def rotLeft(a, d):
    
    collections_deque = deque()

    [collections_deque.append(item) for item in a]

    collections_deque.rotate(-d)
    
    return collections_deque
    

#Input HackerRank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
