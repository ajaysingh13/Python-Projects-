# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 01:47:03 2021

@author: vijay
"""

import Assignment3 as a3


def multiplyList (list2):
    size = len(list2)
    Sum = 1 
    for i in range(size):
        Sum = Sum * list2[i]
   
    print(Sum)
    

multiplyList(a3.listA)