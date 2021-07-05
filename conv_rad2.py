# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:12:06 2021

@author: vijay
"""

import conv_rad1 as convRad

def convec():
    
    heat1 = convRad.convecMeter()
    
    heat1.set_h(10)
    heat1.set_Ts(80)
    heat1.set_Tinf(20)
    heat1.set_D(20)
    heat1.set_A()
    heat1.Set_Qconv()
    
    heat1.printQconv()
    

def heat():
    
    heat2 = convRad.heatLoss()
    
    heat2.set_D(20)
    heat2.set_A()
    heat2.set_Ts(80)
    heat2.set_Tsur(20)
    heat2.set_epsilon()
    heat2.set_Stefan()
    heat2.set_heatLoss()
    
    heat2.printHeatLoss()

convec() 
heat()