#!/bin/python3

import sys
import math
import bisect

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   k = a_i
   l= a_i
   index = 0
   while k>0:
       k= int((l-index+1)/2-1)
    #    print(k)
       if a_t>a[index+k]:
           index = index +k+1
       else:
           l = l-k-index
   if a_i==0 or (index== 0 and a_t<a[0]):
       a.insert(0, a_t)
   else:
       a.insert(index+1, a_t)
   print(a)
   # print('{:.1f}'.format((a[math.ceil((len(a)+1.0)/2)-1] +a[math.floor((len(a)+1.0)/2)-1])/2))
