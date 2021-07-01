# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 18:38:26 2021

@author: vijay
"""

import matplotlib.pyplot as plt
import math

x2 = [1,2,3,4,5,6,7,8,9,10]
y2 = [2,4,6,8,10,12,14,16,18,20]

second_x=len(x2)
second_y=len(y2)


plt.show()
plt.plot(x2,y2,'yellow')
plt.legend(['pedro'])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('yo momma gottem')



plt.show()
plt.scatter(x2,y2)
plt.legend(['your father'])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('yo momma gottem')

for i in range(second_x):
    x2[i] = x2[i] * 5 
    
for i in range(second_y):
    y2[i] = math.sqrt(y2[i])
   
    
plt.show()
plt.plot(x2,y2, 'purple')
plt.legend(['shiny pikachu'])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('yo momma gottem')


plt.show()
plt.scatter(x2,y2)
plt.legend(['legendary zekrom'])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('yo momma gottem')
    

 
