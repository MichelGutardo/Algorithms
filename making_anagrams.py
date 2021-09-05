#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

#>>> My answer
def makeAnagram(a, b):
    idx=0
    count =0
    a_list=list(a)
    b_list=list(b)
    repeated=[]
    
    while idx < len(a_list):
        if a_list[idx] in b_list :
            if(a_list[idx]  not in repeated):
                count_a = a_list.count(a_list[idx]) 
                count_b = b_list.count(a_list[idx])
                repeated.append(a_list[idx])
                if count_a != count_b:
                    count += abs(count_a - count_b) 
        else:
            count+=1
            
        idx+=1
        
    idx =0
    while idx < len(b_list):
        if b_list[idx] not in a_list and b_list[idx] not in repeated :
            count+=1
            
        idx+=1
        
    return count
    
# Input HackerRank    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

    
    
