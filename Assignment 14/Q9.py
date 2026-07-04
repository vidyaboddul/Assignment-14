# Q9. Combined - Properties + Operations + Indexing

# Import NumPy library
import numpy as np

# Generate a 6 x 6 matrix of random numbers
matrix = np.random.randn(6, 6)

# Display the original matrix
print("Original Matrix:")
print(matrix)

# Print the shape, size, and data type
print("\nShape:", matrix.shape)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)

# Find the index of the maximum value
print("\nIndex of Maximum Value:", np.argmax(matrix))

# Find the index of the minimum value
print("Index of Minimum Value:", np.argmin(matrix))

# Extract the top-left 3 x 3 submatrix
print("\nTop-Left 3 x 3 Submatrix:")
print(matrix[:3, :3])

# Replace all negative numbers with their absolute value
matrix = np.abs(matrix)

# Display the modified matrix
print("\nModified Matrix (Negative values converted to Positive):")
print(matrix)

# Print the mean of the modified matrix
print("\nMean of Modified Matrix:", np.mean(matrix))