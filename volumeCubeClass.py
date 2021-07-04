# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:38:09 2021

@author: vijay
"""

#This class is meant to be imported 


class volCube:
    def __init__(self):
        pass
    def set_length(self,length):
        self.length = length
        
    def set_width(self,width):
        self.width = width
        
    def set_height(self,height):
        self.height = height
        
    def set_volume(self):
        self.volume = self.length * self.width * self.height 
        
    def printVol(self):
        print(self.volume)