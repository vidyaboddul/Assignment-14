# Q6. Advanced Indexing

# Import NumPy library
import numpy as np

# Create a 5 x 5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, (5, 5))

# Display the original matrix
print("Original Matrix:")
print(matrix)

# Print the diagonal elements
print("\nDiagonal Elements:")
print(np.diag(matrix))

# Print elements greater than 50
print("\nElements Greater Than 50:")
print(matrix[matrix > 50])

# Replace all elements less than 30 with 0
matrix[matrix < 30] = 0

# Display the modified matrix
print("\nModified Matrix (Elements less than 30 replaced with 0):")
print(matrix)