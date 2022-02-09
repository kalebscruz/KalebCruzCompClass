import matplotlib.pyplot as plt
import numpy as np

theta = np.array(np.arange(0,2 * math.pi, 0.001))
x = 2 * np.cos(theta) + np.cos(2 * theta)
y = 2 * np.sin(theta) - np.sin(2 * theta)
first_example = plt.plot(x, y)