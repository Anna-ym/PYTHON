import numpy as np

# Create a 3x3 matrix using arange and reshape
arr = np.arange(1, 10).reshape(3, 3)

print("Matrix:")
print(arr)

# Sum of all elements
print("\nSum of all elements:", np.sum(arr))

# Sum of each row
print("Sum of each row:", np.sum(arr, axis=1))

# Sum of each column
print("Sum of each column:", np.sum(arr, axis=0))