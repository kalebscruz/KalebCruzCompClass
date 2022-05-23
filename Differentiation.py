import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
from sklearn.preprocessing import normalize

k = 1
def potential(q,r,x,y):
    dif = np.hypot(x-r[0],y-r[1])
    return k*q/(dif+0.001)

grid_x,grid_y = 100,100
x = np.linspace(-50,50,grid_x)
y = np.linspace(-50,50,grid_y)
x_axis,y_axis = np.meshgrid(x,y)

charges = [(-1,(10,0)),(1,(-10,0))]
grid_array = np.zeros((grid_x,grid_y))
electric_potential = 0

for charge in charges:
    electric_potential = potential(*charge,x=x_axis,y=y_axis)
    grid_array += electric_potential 
    
grid = np.gradient(grid_array)

plt.figure(figsize=(10,10))
#norm_grid = norm(grid_array)
gradient_x, gradient_y = np.gradient(grid_array,x,y)
norm_gradient_x = normalize(gradient_x)
norm_gradient_y = normalize(gradient_y)
norm_x_axis = normalize(x_axis)
norm_y_axis = normalize(y_axis)
plt.contour(x_axis, y_axis, grid_array,20,cmap='RdGy')
color = (norm_gradient_x,norm_gradient_y)

plt.colorbar()
plt.quiver(norm_x_axis,norm_y_axis,norm_gradient_x,norm_gradient_y,color='blue')