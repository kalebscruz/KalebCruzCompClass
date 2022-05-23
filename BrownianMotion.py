# -*- coding: utf-8 -*-
"""
Created on Sun May 22 23:29:15 2022

@author: Ksebc
"""


# No idea why everything is to the left side


import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import animation
from matplotlib.animation import FuncAnimation
import random

i,j,n= 50,50, 1000

x_data=[]
y_data=[]


def init():
    line.set_data([],[])
    return line,

def move(i, j):
    direction = random.randint(1, 4)
    if direction == 1 and j < 100 : j += 1 
    elif direction == 2 and j > 0: j -= 1 
    elif direction == 3 and i > 0 : i -= 1 
    elif direction == 4 and i < 100: i += 1
    return (i,j)


def move_animation(i):
    # Attention to these
    x = np.linspace(0,100,100)
    #y = np.sin(2 * np.pi * (x - 0.01 * i))
    y = np.linspace(0,100,100)
    x, y = move(x, y)

    x_data.append(x)
    y_data.append(y)

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line


fig = plt.figure(figsize=(10, 10))
ax = plt.axes(xlim=(0, 10), ylim=(0,10)) 
line, = ax.plot([], [], lw=2, color='#0492C2')

ax.set_xticks(np.arange(0, 101, 50))
ax.set_yticks(np.arange(np.min(0) - 0.5, np.max(100) + 0.5, 0.2))
ax.tick_params(labelsize=16)

anim = animation.FuncAnimation(fig, move_animation, init_func=init, frames=n, interval=20, blit=True)
anim.save('monte_carlo',writer='imagemagick')