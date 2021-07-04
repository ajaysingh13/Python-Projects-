# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 18:53:11 2021

@author: vijay
"""
# creating a class called dog 
class Dog:
    
    # this is a property called x 
    x = 5
    
    
    # intitiating the class "Dog" 
    # this will always execute when you create and object that calls this class 
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    # always include "self" even if you dont need a parameter in the function
    def introduce(self):
        print("Hello, my name is " + self.name)
        
# d1 is an object 
# this object will use the properties inside the class "Dog"
# when you do this, the code will always execute the __init__ method  
d1 = Dog("Fred", 15)

# name is a property  
print(d1.name)

# age is a property 
print(d1.age)
d1.introduce()

# reassigns the vlaue of the age property in the class "Dog" 
d1.age = 20

print(d1.age)

# this calls the property x inside of "Dog"
print(d1.x)