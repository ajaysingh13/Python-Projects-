# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 04:01:57 2021

@author: vijay
"""

import matplotlib.pyplot as plt 

x = []
y = [] 


for u in range(-10,11):
    x.append(u)
    
for l in x:
    y.append(l * l * l)
    
plt.show()
plt.plot(x,y)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('y=x^3')