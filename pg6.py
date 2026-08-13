#create a 2d array using numpy and print it
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
p=np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print(p)
c=arr+p
print("Sum: ",c)
d=arr-p
print("Sub: ",d)
e=arr*p
print("Mul: ",e)
k=np.dot(arr,p)#matrix mul
print("Mul: ",k)
h=np.multiply(arr,p)
print("Mul: ",h)
j=np.transpose(arr)
print("Transpose: ",j)
l=np.transpose(p)
print("Transpose: ",l)
