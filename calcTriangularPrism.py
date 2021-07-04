# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:42:10 2021

@author: vijay
"""
import math

class Volume:
    def __init__(self,a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    
    def printCalc(self):
        x = (1 / 4) * self.h * math.sqrt(- math.pow(self.a,4) + 2 * math.pow((self.a * self.b),2) + 2 * math.pow((self.a * self.c),2) - math.pow(self.b,4) + 2 * math.pow(self.b*self.c,2) - math.pow(self.c,4))
        print(x)
        

wabba = Volume(1,2,2,4)
wabba.printCalc()