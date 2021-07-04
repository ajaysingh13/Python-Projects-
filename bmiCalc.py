# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 17:15:22 2021

@author: vijay
"""
import math

class bmi:
    
    def __init__(self,lbs, inch):
        self.lbs = lbs
        self.inch = inch
        
    def calculate(self):
        self.bmi = (self.lbs / (math.pow(self.inch,2))) * 703
        
    def printBMI(self):
        print("Your bmi is",self.bmi)
        
    def categorize(self):
        if self.bmi < 18.5:
            print("you're literally bones(underweight)")
        if self.bmi >= 18.5 and self.bmi < 25:
            print("you're normal i guess.. (normal weight)")
        if self.bmi >= 25 and self.bmi < 30:
            print("you're slightly fat(overweight)")
        if self.bmi >= 30:
            print("you're fat as fucc(obese)")

x = input("Would you like to enter your info in Metric or Standard? (m for metric/s for standard): ")

if x == "s":
    lbs = int(input("Enter your weight in pounds (lbs):"))
    
    fet = int(input("Enter your height in ft(ft):"))
    inch = fet * 12

    u = int(input("Enter your height in inches(in.):"))
    inch = inch + u 

if x == "m":
    kg = int(input("Enter your weight in kilograms(kg):"))
    lbs = kg * 2.205  
    
    cm = int(input("enter your height in centimeters(cm):"))
    inch = cm / 2.54 

f = bmi(lbs,inch)
f.calculate()
f.printBMI()
f.categorize()