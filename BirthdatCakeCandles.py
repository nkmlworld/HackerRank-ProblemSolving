
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

# def birthdayCakeCandles(candles):
#     # Write your code here
#     count = 0
#     MAX = max(candles)
#     for candle in candles:
#         if candle == MAX:
#             count += 1
#     return count

def birthdayCakeCandles(candles):
    '''n = len(candles)
    maxnum = 0
    count =0
    for  i in range(n):
        if candles[i] > maxnum:
            maxnum = candles[i]
            count = 1
        elif candles[i] == maxnum:
            count += 1
    return count'''
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
