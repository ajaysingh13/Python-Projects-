# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 03:40:44 2021

@author: vijay
"""

import Assignment3 as a3 

def printEvens(list2):
    size = len(list2)
    for i in range(size):
        if list2[i]%2 == 0:
            if list2[i] > 0:
                print(list2[i])



printEvens(a3.listB)