import numpy as np  #numerical python , creating arrays
ax=np.array([1,2,3,4,5,6])
print(ax)
arr=np.arange(1,7)
print(arr)
#shape:2d or 3d predefined variable
print(ax.shape) #6 means no of elements and 1d array(6,)
#reshape:predefined function
a1=ax.reshape(2,3)
print(a1)
print(a1.shape) #2 rows and 3 columns (2,3) and 2d
a2=np.array([10,20,30,40])
print(a2)
print(a2.shape)
a3=a2.reshape(4,1)  #4 rows and 1 column
print(a3)
print(a2.reshape(1,-1)) #1 row and no columns and 1d #array.reshape(1,-1) the parameter 1 make the array have 1 row then -1 automatically calculates the number of columns 
pl=np.array([10,20,30,40,50,60])
print(pl)
print(pl.shape)
px=pl.reshape(1,-1)
print(px)
print(px.shape) #6 columns 