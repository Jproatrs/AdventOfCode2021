# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:57:26 2021

@author: jorge.proano01
"""

import numpy as np
dp=np.loadtxt("input.txt",delimiter="\t",dtype=int)
##### parte1####

s1=0
for x in range(len(dp)-1):
    if np.less(dp[x],dp[x+1]):
        s1=s1+1
print(s1)
##### parte2####

s2=0
t=np.arange(len(dp)-2)
for x in range(len(dp)-2):
    t[x]=dp[x]+dp[x+1]+dp[x+2]
    
for x in range(len(t)-1):
    if np.less(t[x],t[x+1]):
        s2=s2+1
        
print(s2)

#############