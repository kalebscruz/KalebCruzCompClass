import matplotlib.pyplot as plt
import numpy as np
import math
fig, axs = plt.subplots(2,2)
#pulled from geeks for geeks. Not my own
#creates space between each of the plots so theres no overlap.
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

# plot of deltoid curve
part_a_theta = np.array(np.arange(0,2 * math.pi, 0.001))
part_a_x = 2 * np.cos(part_a_theta) + np.cos(2 * part_a_theta)
part_a_y = 2 * np.sin(part_a_theta) - np.sin(2 * part_a_theta)
axs[0,0].plot(part_a_x, part_a_y)
axs[0,0].set_title('Deltoid curve')

# plot of Galilean spiral
part_b_theta = np.array(np.arange(0,10 * math.pi, 0.001))
part_b_r = part_b_theta*part_b_theta
part_b_x =part_b_r*np.cos(part_b_theta)
part_b_y =part_b_r*np.sin(part_b_theta)
axs[0,1].plot(part_b_x,part_b_y)
axs[0,1].set_title('Galilean spiral')

# plot of "fey's function"
part_c_theta = np.array(np.arange(0,24*math.pi,0.001))
part_c_r = pow(10,np.cos(part_c_theta))*2*np.cos(4*part_c_theta)+np.sin(part_c_theta/12)**5
part_c_x = part_c_r *np.cos(part_c_theta)
part_c_y = part_c_r * np.sin(part_c_theta)
axs[1,0].plot(part_c_x, part_c_y)
axs[1,0].set_title('Feys function')

plt.plot()
