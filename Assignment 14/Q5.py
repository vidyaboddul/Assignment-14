# Q5. NumPy Indexing - 1D & 2D

# Import NumPy library
import numpy as np

# Create the given 2D array
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

# Display the original array
print("Original Array:")
print(arr)

# Extract the first row
print("\nFirst Row:")
print(arr[0])

# Extract the last column
print("\nLast Column:")
print(arr[:, -1])

# Extract the center 2 x 2 submatrix
print("\nCenter 2 x 2 Submatrix:")
print(arr[1:3, 1:3])

# Extract all even numbers using boolean indexing
print("\nEven Numbers:")
print(arr[arr % 2 == 0])