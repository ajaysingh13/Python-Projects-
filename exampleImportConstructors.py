7# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:39:05 2021

@author: vijay
"""

import volumePrismClass as prism 

def calcVolCube():
    length = 5 
    width = 3
    height = 2
    
    #this is slightly different from before 
    #used to be vol_1 = volCube() before using import
    vol_1 = prism.volCube()
    
    #this is same as before 
    vol_1.set_length(length)
    vol_1.set_width(width)
    vol_1.set_height(height)
    vol_1.set_volume()
    
    vol_1.printVol()

def calcVolCone():
    radius = 7
    height = 5
    
    vol_2 = prism.volCone()
    vol_2.set_height(height)
    vol_2.set_radius(radius)
    vol_2.set_volume()
    
    vol_2.printVol()
    
    
#MAIN FUNCTION
calcVolCube()
calcVolCone()