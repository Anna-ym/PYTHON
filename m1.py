#to read no of rows and columns for matrix1
#create a matrix1 
#to read no of rows and columns for matrix2
#create a matrix2
#find dot product ,transpose,trace
#find rank of m1 and m2
#find the determinant of m1
#find the inverse of m2
import numpy as np
r1=int(input("Enter the number of rows: "))
c1=int(input("Enter the number of columns: "))
m1=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        val=int(input("Enter elements: "))
        row.append(val)
    m1.append(row)
m1=np.array(m1)   

r2=int(input("Enter the number of rows: "))
c2=int(input("Enter the number of columns: "))
m2=[]
for i in range(r2):
    row=[]
    for j in range(c2):
        val=int(input("Enter elements: "))
        row.append(val)
    m2.append(row)
m2=np.array(m2)     

print(m1)
print(m2)

print("Dot Product:\n", np.dot(m1, m2))
print("Transpose m1:\n", np.transpose(m1))
print("Transpose m2:\n", np.transpose(m2))
print("Trace Matrix 1:", np.trace(m1))
print("Trace Matrix 2:", np.trace(m2))
print("Rank of Matrix 1:", np.linalg.matrix_rank(m1))
print("Rank of Matrix 2:", np.linalg.matrix_rank(m2))
print("Determinant of Matrix 1:", np.linalg.det(m1))
print("Inverse of Matrix 2:\n", np.linalg.inv(m2))