# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:10:35 2021

@author: vijay
"""

import math

class convecMeter():
    
    def __init__(self):
        pass
    
    def set_h(self,h):
        self.h = h
    
    def set_Ts(self,Ts):
        self.Ts = Ts + 273
        
    def set_Tinf(self,Tinf):
        self.Tinf = Tinf + 273
        
    def set_D(self,D):
        self.D = D / 1000
        
    def set_A(self):
        self.A = math.pi * self.D 
        
    def Set_Qconv(self):
        self.Qconv = self.h * (self.Ts - self.Tinf) * self.A 
        self.Qconv = round(self.Qconv, 2)
        
    def printQconv(self):
        print("yo betch, the heat loss by convection per meter length of pipe is:", self.Qconv)
        

class heatLoss():
    
    def __init__(self):
        pass 
    
    def set_D(self,D):
        self.D = D / 1000
    
    def set_A(self):
        self.A = math.pi * self.D
    
    def set_Ts(self,Ts):
        self.Ts = Ts + 273
    
    def set_Tsur(self,Tsur):
        self.Tsur = Tsur + 273
    
    def set_epsilon(self):
        self.epsilon = 1
        
    def set_Stefan(self):
        self.Stefan = 5.67 * math.pow(10,-8)
        
    def set_heatLoss(self):
        self.heatLoss = self.epsilon * self.Stefan * (math.pow(self.Ts,4) - math.pow(self.Tsur,4)) * self.A
        self.heatLoss = round(self.heatLoss,2)
        
    def printHeatLoss(self):
        print("yo betch, the heat loss due to radiation is:",self.heatLoss)