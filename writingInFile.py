# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:33:30 2021

@author: vijay
"""


#"a" means append, we will beginning appending to the end of the file
f = open("writeFileExample.txt","a")

#adding a "\n" to the write function, the written line appended
#will be on a new line 
f.write("\nThis will be written on a new line")
f.close()

#open and read the file after the appending 
f = open("writeFileExample.txt","r")
print(f.read())
f.close()