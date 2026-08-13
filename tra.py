#trace of a matrix
import numpy as np
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# Calculate the trace (1 + 5 + 9 = 15)
matrix_trace = np.trace(matrix)
print(matrix)

print("\nTrace of the Matrix:", matrix_trace)