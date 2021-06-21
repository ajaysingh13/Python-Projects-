# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:10:19 2021

@author: vijay
"""

prices = [13.49, 8.99, 4.99, 6.49, 20.49, 16.99, 3.99, 5.99, 11.99, 5.00, 10.00]

size = len(prices)

for i in range(size):
    if prices[i] < 10:
        if prices[i] > 5:
            print(prices[i])