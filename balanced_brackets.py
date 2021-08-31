#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# >>>> My answer
def isBalanced(s):
    opened =[]
    
    if(s[0] in "}])" ):
        return "NO"
    
    for char in s:
        
        if(char in ("{([")):
            opened.append(char)
            continue
    
        if(len(opened) > 0 ):
            
            if(char=="]" and opened[-1] =="["):
                del opened[-1]
                continue
            elif(char=="}" and opened[-1] =="{"):
                del opened[-1]
                continue
            elif(char==")" and opened[-1] =="("):
                del opened[-1]
                continue
            else:
                return "NO"
        else:
            return "NO"
    
    if len(opened) >0:
        return "NO"
    else:
        return "YES"
                

#Input HackerRank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
