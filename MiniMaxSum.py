#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#approach 1
# def miniMaxSum(arr):
#     print(sum(arr)-max(arr), sum(arr)-min(arr))

# def miniMaxSum(arr):
#     # Write your code here
#     sums = []
#     for i in range(5):
#         for j in range(1):
#             sums.append(sum(arr)-arr[i])
#     print(min(sums), max(sums))

def miniMaxSum(arr):
    s = 0
    minnum = 9999999999999
    maxnum = 0
    n = len(arr)
    for i in range(n):
        s += arr[i]
        minnum = min(minnum, arr[i])
        maxnum =  max(maxnum, arr[i])
        
    print(s-maxnum, s-minnum)

if __name__ == '__main__':
    
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
