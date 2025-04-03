#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'migratoryBirds' function below.

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


# def migratoryBirds(arr):
#     # Write your code here
#     l = [0] * len(arr)
    
#     for i in range(len(arr)):
#         l[arr[i]] += 1
    
#     return l.index(max(l))

def migratoryBirds(arr):
    bird_count = {}  # Dictionary to count occurrences of each bird type

    # Count occurrences of each bird type
    for bird in arr:
        bird_count[bird] = bird_count.get(bird, 0) + 1

    # Find the maximum frequency
    max_frequency = max(bird_count.values())

    # Find the smallest bird type ID with the maximum frequency
    return min(bird for bird in bird_count if bird_count[bird] == max_frequency)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
