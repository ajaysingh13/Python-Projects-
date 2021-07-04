# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:11:53 2021

@author: vijay
"""

listA = [2, 6, 1, 8, 2, 11, 17, -4, 8, 1, 11]
listBruh = []
size = len(listA)
for i in range(size):
    counter = 0
    temp = listA[i]
    for x in range(size):
        if temp == listA[x]:
            counter = counter + 1
    if counter == 1:
        listBruh.append(temp)
            
                