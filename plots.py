# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:06:34 2021

@author: vijay
"""

import matplotlib.pyplot as plt 

time = [0, 1, 2, 3, 4]

position = [0, 2, 4, 6, 8]

plt.show()
plt.plot(time, position)
plt.xlabel('Time (s)')
plt.ylabel('Postition (m)')

plt.show()
plt.scatter(time, position)
plt.xlabel('Time (s)')
plt.ylabel('Postition (m)')

