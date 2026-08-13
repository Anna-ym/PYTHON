#find the determinant of an array matrix
import numpy as np

matrix = np.array([[1, 2],[3, 4]])
det = np.linalg.det(matrix)
print("Matrix:")
print(matrix)
print("\nDeterminant:", det)