#!/bin/python3

import sys
import math
import bisect

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   if a_i==0 or (a_t<a[0]):
      a.insert(0, a_t)
   else:
       k = a_i-1
       j = 0
       while j<k:
           mid= int((k-j+1)/2)
       #    print(k)
           if a_t>a[j+mid]:
               j = j+mid
           else:
               k = j+mid-1
       a.insert(j+1, a_t)
   # print(a)
   print('{:.1f}'.format((a[math.ceil((len(a)+1.0)/2)-1] +a[math.floor((len(a)+1.0)/2)-1])/2))
