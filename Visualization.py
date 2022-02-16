import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

part_a_theta = np.array(np.arange(0,2 * math.pi, 0.001))
part_a_x = 2 * np.cos(part_a_theta) + np.cos(2 * part_a_theta)
part_a_y = 2 * np.sin(part_a_theta) - np.sin(2 * part_a_theta)
plt.plot(part_a_x, part_a_y)


part_b_theta = np.array(np.arange(0,10 * math.pi, 0.001))
r=part_b_theta*part_b_theta
part_b_x=r*np.cos(part_b_theta)
part_b_y=r*np.sin(part_b_theta)
plt.plot(part_b_x,part_b_y)

def third_part():
    part_c_theta = np.array(np.arange(0,24*math.pi,0.001))
    r = pow(10,np.cos(part_c_theta))*2*np.cos(4*part_c_theta)+np.sin(part_c_theta/12)**5
    part_c_x = r *np.cos(part_c_theta)
    part_c_y = r * np.sin(part_c_theta)
    plt.plot(part_c_x, part_c_y)
