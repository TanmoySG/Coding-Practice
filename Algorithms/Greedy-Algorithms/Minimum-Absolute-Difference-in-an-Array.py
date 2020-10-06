#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    #arr = [i for i in itertools.combinations(arr, 2)]
    minimum = abs(arr[0]-arr[1])
    for i in range(len(arr)-1):
        minimum = min(minimum, abs(arr[i]-arr[i+1]))
    return minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
