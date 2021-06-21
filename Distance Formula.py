# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:37:19 2021

@author: vijay
"""
import math

D = [0] * 10

x1 = [1,1,1,1,1,1,1,1,1,1]  
x2 = [1,2,3,4,5,6,7,8,9,10]
y1 = [1,1,1,1,1,1,1,1,1,1]
y2 = [2,4,6,8,10,12,14,16,18,20]

first_x = len(x1)

for i in range(first_x):
     D[i] = math.sqrt(math.pow(x2[i]-x1[i],2) + math.pow(y2[i]-y1[i],2))
     
print(D) 
                         

                         
     
                     
    
