# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:56:27 2021

@author: vijay
"""

#this is reading from a test file called "Helloworld.txt"

f = open("yoMomma!!.txt", "r")

#f.read() reads the entire file
print(f.read())

# read lines of the file
#print(f.readline())
#print(f.readline())

#this will close the file when we are finished with it
f.close()