# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:43:20 2021

@author: vijay
"""

a = [4, 8, 21, 87, -23, 0, 43] 

size = len(a)

max_num = a[0]

for i in range(size):
    if a[i] > max_num:
        max_num = a[i]
        
print(max_num)

min_num = a[0]

for j in range(size):
    if a[j] < min_num:
        min_num = a[j]

print(min_num)

