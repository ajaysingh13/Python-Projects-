# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:27:45 2021

@author: vijay
"""

#ultility functions 
def subtotal(total, quantity, price):
    total = total + (quantity * price)
    return total 

def promptFruit(name, price, total):
    print('Hey fatty do you want', name, '(y/n)')
    t = input()
    
    if (t == 'y'):
         print('bueerg how many', name)
         u = int(input())
         total = subtotal(total, u, price)
         return total 
    else:
        return 0
    
def calcTax(total, taxRate):
    temp = total * taxRate 
    total = total + temp 
    return total

#prices of fruit 
banana = 2
orange = 1 
apple = 3 
watermelon = 5
durian = 15
dragonfruit = 30
grape = 12

taxRate = .05

total = 0