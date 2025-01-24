#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

# def kangaroo(x1, v1, x2, v2):
#     # Write your code here
#     j1=0
#     j2=0
#     c=0
#     if x1<x2 and v1<v2:
#         return "NO"
#     else:
#         for _ in range(1):
#             j1 = x1 + v1
#             j2 = x2 + v2
#             if j1 == j2:
#                 return "YES"
                
#         for _ in range(10000):
#             j1 += v1
#             j2 += v2
#             c+=1
#             if j1 == j2:
#                 print("c", c)
#                 return "YES"
                
def kangaroo(x1, v1, x2, v2):
  if x1 < x2 and v1 < v2:
    return "NO"
  else:
    if v1!=v2 and (x2-x1)%(v1-v2)==0:
      return "YES"
    else:
      return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
