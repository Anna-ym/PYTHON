#numpy pgm to create a 5*5 zero matrix on the main diagonal=1,2,3,4,5
import numpy as np
arr=np.zeros((5,5),int)
print(arr)
print(np.diag([1,2,3,4,5]))