# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:01:05 2022

@author: Ksebc
"""

import numpy as np
import random as rand

n = 1000000

random_numbers = np.zeros(n)
probability_distribution = np.zeros(n)

def p(x):
    return 1 / (np.sqrt(x))

for i in range(n):
    random_numbers[i] = rand.uniform(0,1)
    probability_distribution[i] = random_numbers[i]**(-1/2)
    
mean = np.mean(p(probability_distribution))

print(mean)