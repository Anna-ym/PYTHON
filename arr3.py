#numpy pgm to create an array matrix and to compute sum of all elements ,sum of each column and sum of each row
import numpy as np
a1=np.array([10,20,30,40,50,60,70,80,90])
print(a1.reshape(3,3))
print(np.sum(a1))
print(np.sum(a1,axis=0))
print(np.sum(a1,axis=1))
