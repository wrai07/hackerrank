#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count=0
    i=0
    while i< len(arr):
        index=arr[i]-1   # n= arr[i] index=n-1=arr[i]-1 
       # print('bef=',arr,i)
        if arr[i]!=arr[index]: #n!=[n-1]
            arr[i],arr[index]=arr[index],arr[i]
            count+=1
        else:
            i+=1
       # print('aft=',arr)    
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


# In[ ]:





# In[ ]:




