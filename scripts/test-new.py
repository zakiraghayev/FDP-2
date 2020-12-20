import matplotlib.pyplot as plt
import numpy as np

from kriging import OK



np.random.seed(123433789) # GIVING A SEED NUMBER FOR THE EXPERIENCE TO BE REPRODUCIBLE
grid = np.zeros((10,10),dtype='float32') # float32 gives us a lot precision
# x,y = np.array([600,400,800,600,500,800]), np.array([800,700,400,600,400,800]) # CREATE POINT SET.
x,y = np.array([10,20,30,40,50,60,70,80]), np.array([1,2,3,4,5,6,7,8]) # CREATE POINT SET.
v = np.array([0.2,0.21,0.2,0.25,0.29,0.24, 0.29,0.24]) # THIS IS MY VARIABLE
# v = np.random.randint(100,1000,6) # THIS IS MY VARIABLE
# print(grid)
grid = OK(x,y,v,(50,30),grid)
plt.imshow(grid.T,origin='lower',interpolation='nearest',cmap='jet')
plt.scatter(x, y, c=v, s=20)
# plt.xlim(0,grid.shape[0])
# plt.ylim(0,grid.shape[1])
plt.grid()
plt.show()
