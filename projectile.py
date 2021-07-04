# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:56:04 2021

@author: vijay
"""
import math

g = 9.81
v0 = int(input("Enter the intial launch velocity (m/s): " ))
theta = int(input("Enter the intial launch angle (degrees): "))
theta = math.radians(theta)
Range = math.pow(v0,2) * math.sin(2 * theta) / g 
vx0 = v0 * math.cos(theta)
vy0 = v0 * math.sin(theta)
t = Range / vx0
h = (vy0 * (t / 2)) - ((1/2) * g * math.pow((t/2),2))

print("Calculating...")
print("Range: ", Range)
print("Air time: ", t)
print("Maximum height: ", h)