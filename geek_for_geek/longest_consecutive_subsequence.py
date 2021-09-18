#!/bin/python3
#User function Template for python3
 
# >>> My answer
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        arr.sort()
        largest = [1]
        count=0
        idx = 0
        
        while idx < N:

            if(arr[idx-1]!=arr[idx]):
                count+=1

            if(idx==N-1 ):
                largest.append(count)
                break
            elif idx+1 <N:
                if (arr[idx+1] -arr[idx] > 1):
                    largest.append(count)    
                    count=0
            idx += 1
            

        return max(largest)    


# Input GFG

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends