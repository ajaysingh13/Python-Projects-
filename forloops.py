# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:23:03 2021

@author: vijay
"""
import matplotlib.pyplot as plt 

fruitlist = ['banana', 'orange', 'apple', 'watermelon']

"""
# for loop
for x in fruitlist:
    print (x)
    
    if (x == 'apple'):
        print('this is an apple')
 
for x in range (1,11):
    print(x)
        
"""

y= []
x = []
z = []

for i in range(1,101):
    x.append(i)
    
for j in x:
    y.append(j * j)
    
for k in x:
    z.append(1 / k)
    
plt.show()
plt.plot(x,y)

plt.show()
plt.plot(x,z)