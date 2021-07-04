# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:08:50 2021

@author: vijay
"""
import math

class Reverse:
    
    def __init__(self,inputt):
        self.inputt = inputt
        
    def reeverse(self):
        newList = []
        size = len(self.inputt)
        
        for i in range(size):
            newList.append(self.inputt[i])
            
        for i in range(math.floor(size/2)):
            temp = newList[i]
            newList[i] = newList[size-1-i]
            newList[size-1-i] = temp

        print(newList)

wabba = Reverse("littleCaesers")    
wabba.reeverse()