# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 19:16:50 2021

@author: vijay
"""

# this is the parent class 
class Person:
    def __init__ (self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printName(self):
        print(self.firstname, self.lastname)

# this is a child class, it inherits properties from the "Person" class 
class Student(Person):
    def __init__(self, fname, lname, year):
        # super will allow Student to inherit the properties in the class "Person" 
        # those properties include self.firstname and self.lastname 
        super().__init__(fname, lname)
        self.graduationyear = year


x = Person("ajay","singh")
x.printName()

# Student uses "Person" class 
p = Student("yo","momma", 1678)
p.printName()

x = Student("mike","tyson",2000)

x.printName()