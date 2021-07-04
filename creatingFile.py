# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:43:27 2021

@author: vijay
"""

#"x" is used to create files
#f = open("createdFile.txt","x")
#f.close()
#commented this section out because pythin will error if
#we attempt to create a file that already exists

#"w" is overwriting the "createdFile.txt" text file with
#the following two lines of code 
f = open("createdFile.txt","w")
f.write("This is the first line")
f.write("\nThis is the second line")
f.close()