import numpy as np
import matplotlib.pyplot as plt

k = 1
def potential(q,r,x,y):
    dif = np.hypot(x-r[0],y-r[1])
    return k*q/(dif+0.001)


grid_x,grid_y = 100,100
x = np.linspace(-50,50,grid_x)
y = np.linspace(-50,50,grid_y)
x_axis,y_axis = np.meshgrid(x,y)

charges = [(-1,(5,0)),(1,(-5,0))]
grid_array = np.zeros((grid_x,grid_y))
electric_potential = 1
for charge in charges:
    electric_potential = potential(*charge,x=x_axis,y=y_axis)
    grid_array += electric_potential
    
fig = plt.figure(figsize=(7,7))
plt.contour(x_axis,y_axis,grid_array,20,cmap='RdGy')
plt.colorbar()

gradient_x, gradient_y = np.gradient(grid_array,x,y)

fig = plt.figure(figsize=(10,10))
color = np.log(np.hypot(gradient_x,gradient_y))
ax = fig.add_subplot()
ax.streamplot(x_axis,y_axis, gradient_x,gradient_y, linewidth = 1, cmap=plt.cm.inferno, arrowstyle = '->', arrowsize = 1)
#Figure out how to create the full graph