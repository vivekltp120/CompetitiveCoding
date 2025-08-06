#find the sum of submatrix

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum():
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    i=0
    j=0
    hsumarr=[]
    while True:
        hsum=0
        for x in range(i,i+3):
            for y in range(j,j+3):
                print((x,y))
                hsum+=arr[x][y]

        hsum=hsum-arr[(i+i+2)//2][j]-arr[(i+i+2)//2][j+2]
        hsumarr.append(hsum)
        j+=1
        if j>3:
            i+=1
            j=0
        if i>3:
            break
    return max(hsumarr)
#Tokenize the sentences and remove punctuation symbol and convert in lower case
def tokenizer():
    list_of_sentences=[]
    fp=open('tokenizer_input.txt','r')
    list_of_sentences.extend(fp.readlines())
    print(list_of_sentences)
    print(len(list_of_sentences))
    tokenlist=[]
    for x in list_of_sentences:
        x.lower()
        tokenlist.extend(re.split('.\n',x))
    print(tokenlist)


# Complete the arrayManipulation function below.
def arrayManipulation():
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))




    max_val = 0
    qlist=[]
    qk={}
    print(qlist)
    for i in range(len(queries)):
        si, ei, kv = list(map(int, queries[i]))
        temp_set = set([x  for x in range(si, ei + 1)])
        qlist.append(temp_set)
        qk.__setitem__(temp_set,kv)
    for x in qlist:
        pass

    print (max_val)


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s.endswith('PM'):
        s = s.rstrip('PM')
        s = [int(x) for x in list(s.split(":"))]
        if s[0] < 12:
            s[0] = 12 + s[0]
        return ":".join([str(x).zfill(2) for x in s])

    if s.endswith('AM'):
        s = s.rstrip('AM')
        s = [int(x) for x in list(s.split(":"))]
        if s[0] == 12 or s[0] == 24:
            s[0] = 0
        return ":".join([str(x).zfill(2) for x in s])



if __name__ == '__main__':
    # result = hourglassSum()
    # print(result)
    # tokenizer()
    # arrayManipulation()
    #Time Conversion
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
