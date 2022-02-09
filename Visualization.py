import matplotlib.pyplot as plt
import numpy as np

theta = np.array(np.arange(0,2 * math.pi, 0.001))
x = 2 * np.cos(theta) + np.cos(2 * theta)
y = 2 * np.sin(theta) - np.sin(2 * theta)
plt.plot(x, y)

new_theta = np.array(np.arange(0,10 * math.pi, 0.001))
r=theta*theta
new_x=r*np.cos(theta)
new_y=r*np.sin(theta)
plt.plot(new_x,new_y)
plt.show()
