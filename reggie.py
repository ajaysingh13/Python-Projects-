# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:57:08 2021

@author: vijay
"""

class Reggie:
    
    def __init__(self,fname,lname, cs, gyear, idd):
        self.fname = fname
        self.lname = lname
        self.cs = cs
        self.gyear = gyear 
        self.idd = idd
        
    def Studento(self):
        print("My name is",self.fname,self.lname,". I am a", self.cs, "and I graduate in", self.gyear,".")
        print("My ID # is",self.idd)
        
ajay = Reggie("Ajay","Singh","10th",2024,82011913)
ajay.Studento()