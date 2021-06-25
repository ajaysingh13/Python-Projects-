# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:23:56 2021

@author: vijay
"""

#prices of fruits 
banana = 2
orange = 1 
apple = 3 
watermelon = 5 
total = 0

"""
# if else 
if banana < watermelon:
    # if the value of banana is less then watermelon 
    print('banana is less than watermelon')
elif banana == watermelon:
    print('banana is the same as watermelon')
else:
    print('banana is greater than watermelon')
    
"""

z = input('Would you like anything? (y/n) ')

if z == 'y':
    print('welcome to the store...')
    t = input('would you like bananas? (y/n) ')
    if t == 'y':
        u = int(input('how many bananas? '))
        total = total + (u * banana)
        
    t = input('Would you like oranges? (y/n) ')
    if t == 'y':
        u = int(input('how many oranges? '))
        total = total +  (u * orange)
        t = input('Would you like apple? (y/n) ')
    if t == 'y':
        u = int(input('how many apples? '))
        total = total +  (u * apple)
        t = input('Would you like watermelons? (y/n) ')
    if t == 'y':
        u = int(input('how many watermelons? '))
        total = total +  (u * watermelon)
        
    print('hey loser, your total is',total)
        
    
elif z == 'n':
    print('peace loser!')