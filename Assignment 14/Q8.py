# Q8. Matrix Multiplication

# Import NumPy library
import numpy as np

# Create two 3 x 3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Display the matrices
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Element-wise multiplication
# Multiplies each element of A with the corresponding element of B
elementwise = A * B

print("\nElement-wise Multiplication:")
print(elementwise)

# Matrix multiplication
# Multiplies rows of A with columns of B
matrix_mult = A @ B
# You can also use: np.dot(A, B)

print("\nMatrix Multiplication:")
print(matrix_mult)