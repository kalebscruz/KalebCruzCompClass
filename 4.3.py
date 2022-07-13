# -*- coding: utf-8 -*-
"""
Created on Mon May 23 00:21:16 2022

@author: Ksebc
"""

import numpy as np
import matplotlib.pyplot as plt


def derivative(f, delta, x):
    deriv = (f(x + delta) - f(x)) / delta
    return deriv

def func(x):
    function = x * (x-1)
    return function


print(derivative(func, 10e-2, 1))
print(derivative(func, 10e-4, 1))
print(derivative(func, 10e-6, 1))
print(derivative(func, 10e-8, 1))
print(derivative(func, 10e-10, 1))
print(derivative(func, 10e-12, 1))
print(derivative(func, 10e-14, 1))


x_vals = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
y_vals = [derivative(func, x, 1) for x in x_vals]


plt.scatter(x_vals,y_vals)

plt.show()

#I think when computer error plays a part in why theres a difference
