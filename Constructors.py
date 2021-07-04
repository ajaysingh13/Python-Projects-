# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 19:57:03 2021

@author: vijay
"""

#object-oriented programming 

class Introductions: 
    
    
    def __init__(self, str1):
        self.Name = str1
        
    #parameterized constructor
    def printAge(self,age):
        self.age = age
        print("I am ", self.age, "years old")
       
    #default constructor
    #this method does not take any arguments
    def introduce(self):
        print("Hello my name is", self.Name)

#creating objects of the class "Introductions"        
ajay = Introductions("ajay")

#call the instance method using the object "Intro" 
ajay.introduce()

#invoking parameterized constructor
ajay.printAge(14)

tobi = Introductions("tobi")

tobi.introduce()

tobi.printAge(15)