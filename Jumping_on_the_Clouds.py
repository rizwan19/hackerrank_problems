#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    size_of_c = len(c)
    count=item=0
    while item<size_of_c:
        if item==size_of_c-1:
            break
        if item+2<size_of_c and c[item+2]!=0:
            item+=1
            count+=1
        elif item+2<size_of_c:
            count+=1
            item+=2 
        else:
            count+=1
            break
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
