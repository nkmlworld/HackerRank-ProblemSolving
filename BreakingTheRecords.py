#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    mincount = maxcount = 0
    minscore = maxscore = scores[0]
    
    for curr_score in scores:
        if minscore < curr_score:
            minscore = curr_score
            mincount += 1
        elif maxscore > curr_score:
            maxscore = curr_score
            maxcount += 1
    return mincount, maxcount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
