# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:19:05 2022

@author: Ksebc
"""

import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

SOLAR_MASS = 1.898e30 #Our sun's mass kg
GRAVITATIONAL_CONSTANT = 6.674e-10 #m^3 * kg^-1 * s^-2
GM = (GRAVITATIONAL_CONSTANT * SOLAR_MASS)

#Example of orbit

earth_mass = 1.67e-27 #Proton mass kg
earth_sun_distance = 1.58e11 #Earth to sun distance meters
earth_velocity = 3.0e4  #m/s place holder

iterations = 1000
n = 1e-15

#Each component of the hyperbolic approach equation
#There are two ways to calculate the angle phi depending on what information
#you are given
def calculate_phi(particle_velocity,particle_distance):
    phi = mp.degrees(mp.acot((particle_velocity**2 * particle_distance)/GM))
    return phi

def calculate_alpha(particle_mass):
    return GRAVITATIONAL_CONSTANT * particle_mass * SOLAR_MASS

def calculate_momentum(particle_mass,particle_velocity):
    return 1/2 * particle_mass * particle_velocity**2

def calculate_energy(particle_mass,particle_velocity,particle_distance):
    return particle_mass * particle_velocity * particle_distance

def rmin(alpha, momentum):
    return -alpha/(2 * momentum)*(1 - np.e)

random_velocity = np.random.randn(iterations,1)
random_distance = np.random.rand(iterations, 1)
random_mass = np.random.randn(iterations,1)

x = np.arange(0,np.amax(random_mass),1000)

phi_array_fixed_distance = np.zeros(iterations)
phi_array_random_distance = np.zeros(iterations)

for i in range(iterations):
    phi_array_random_distance[iterations] = 1e13 * calculate_phi(earth_velocity,random_distance)
    phi_array_fixed_distance[iterations] = 1e13 * calculate_phi(random_mass,random_distance)
    
plt.xlim(0,iterations)
plt.ylim(0,n)

fig_phi_fixed_distance = plt.scatter(x, phi_array_fixed_distance(x))
fig_phi_random_distance = plt.scatter(x,phi_array_random_distance(x))

plt.show(fig_phi_fixed_distance,fig_phi_random_distance)





