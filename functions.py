# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 01:48:18 2021

@author: vijay
"""

import math

#this is where our function goes
def printWorld():
    print('printing from a function')

#this function adds two numbers and prints the sum 
def addInt(x,y):
    z = x + y 
    print(z)
 
#this function finds the bigger of two numbers 
def findMax(a,b):
    if (a > b):
        print (a)
    elif (b > a):
        print (b)
    else:
        print(a)
        
#this function returns a max number
def assignMax(r,t):
    if (a > b):
        return a
    elif (b > a):
        return b
    else:
        return a
    
def function1():
    return 20

def yomomma(g):
     g = math.pow(g,2)
     return g 
   
def squareRoot(h):
    h = math.sqrt(h)
    return h

#this is our main function 
a = 2 
b = 10

#printWorld()
#addInt(a,b)

#findMax(3, 6)

x = assignMax(a, b)

y = function1()

z = yomomma(5)

u = squareRoot(100)