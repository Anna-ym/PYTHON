#numpy pgm to save a given array to a text file and load it ,dtype=,astype(int 64)
import numpy as np
arr=np.arange(1,10)
print(arr)
np.savetxt("neww.txt",arr,fmt="%d")
x=np.loadtxt("neww.txt")
print(x)