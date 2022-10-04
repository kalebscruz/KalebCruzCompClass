# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 06:21:24 2022

@author: Ksebc
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1000)

plt.plot(x, signal.square(2*np.sin(x/100))) #square wave

plt.show()

plt.plot(x, signal.sawtooth(2*np.sin(x)))

plt.show()

plt.plot(x, np.sin(np.pi * x / 1000) * np.sin(20 * np.pi * x / 1000))

plt.show()

