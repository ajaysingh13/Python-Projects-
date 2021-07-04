# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:28:30 2021

@author: vijay
"""
import math


'''
def SqrtRtTkr (a):
    a = math.sqrt(a)
    return a 

x = SqrtRtTkr(4)
print(x)
'''

def findingMax (a, b, c):
    if a > b:
        if a > c:
            return a 
    if b > a:
        if b > c:
            return b 
    if c > a:
        if c > b:
            return c
         
def findingMax (a, b, c, d):
    if a > b:
        if a > c:
            if a > d:
                return a 
    if b > a:
        if b > c:
            if b > d:
                return b 
    if c > a:
        if c > b:
            if c > d:
                return c
    if d > a:
        if d > b:
            if d > c:
                return d
    

    
def calcSum(list1):
    size = len(list1)
    Sum = 0
    for i in range(size):
        Sum = Sum + list1[i]
        
    print(Sum)
    


list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
calcSum(list1)

d = findingMax(5, 6, 2, 10)
print(d)


    
