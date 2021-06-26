# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 02:18:28 2021

@author: vijay
"""

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

z = input('Would you like anything? (y/n) ')

if z == 'y':
    print('welcome to the store...')
    
    total = promptFruit('bananas', banana, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = promptFruit('oranges', orange, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = promptFruit('apples', apple, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = promptFruit('watermelons', watermelon, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = promptFruit('durians', durian, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = promptFruit('dragonfruits', dragonfruit, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = promptFruit('grapes', grape, total)
    print('Hey broke bitch your subtotal is --', total)

    print('hey loser, your total is',total, 'before taxes...')
    
    total = calcTax(total, taxRate)
    
    print('your new total after taxes you bum is', total)

            
elif z == 'n':
    print('peace loser!')
    
