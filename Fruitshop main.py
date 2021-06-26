# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:29:22 2021

@author: vijay
"""

import fruitshoputil as util 

total = 0 

z = input('Would you like anything? (y/n) ')

if z == 'y':
    print('welcome to the store...')
    
    total = util.promptFruit('bananas', util.banana, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = util.promptFruit('oranges', util.orange, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = util.promptFruit('apples', util.apple, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = util.promptFruit('watermelons', util.watermelon, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = util.promptFruit('durians', util.durian, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = util.promptFruit('dragonfruits', util.dragonfruit, total)
    print('Hey broke bitch your subtotal is --', total)
    
    total = util.promptFruit('grapes', util.grape, total)
    print('Hey broke bitch your subtotal is --', total)

    print('hey loser, your total is',total, 'before taxes...')
    
    total = util.calcTax(total, util.taxRate)
    
    print('your new total after taxes you bum is', total)

            
elif z == 'n':
    print('peace loser!')