# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:07:40 2022

@author: Ksebc
"""

import numpy as np
import matplotlib.pyplot as plt

w = 0.001
V = 20
mass = 9.12e-31
plancks = 6.626e-34

E = np.linspace(0,20)

def y1(E):
    return np.tan(np.sqrt(w ** 2 * mass * E / 2 * plancks **2))
def y2(E):
    return np.sqrt((V - E)/E)
def y3(E):
    return - np.sqrt(E/(V-E))

plt.plot(E,y1(E))
plt.plot(E,y2(E))
plt.plot(E,y3(E))

estimates = np.zeros(6)

for i in range (6):
    estimates[i] = y1(i)
    
print(estimates)
