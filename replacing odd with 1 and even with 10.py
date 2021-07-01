# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:01:14 2021

@author: vijay
"""

x = [-8, 12, 65, 23, 908, 34, 23, -57, 87, 4, 3 ,354 ,-45, 23, 567, 76, 45 ,57, 7]
print(x)

size = len(x)

for i in range(size):
    if x[i]%2 == 0:
        x[i] = 10
    if x[i]%2 == 1:
        x[i] = 1
print(x)
