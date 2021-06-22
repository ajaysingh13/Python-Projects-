# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 19:56:30 2021

@author: vijay
"""

import math

import Assignment3 as a3
size = len(a3.x1)

D = [0] * size


for i in range(size):
    D[i] = math.sqrt(math.pow(a3.x2[i]-a3.x1[i],2) + math.pow(a3.y2[i]-a3.y1[i],2))
    
print(D)
