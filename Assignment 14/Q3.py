# Q3. Statistical Methods on 2D Array

# Import NumPy library
import numpy as np

# Create a 4x5 matrix with random integers between 20 and 80
matrix = np.random.randint(20, 81, (4, 5))

# Display the matrix
print("4 x 5 Matrix:")
print(matrix)

# Print the minimum and maximum values
print("\nMinimum value:", np.min(matrix))
print("Maximum value:", np.max(matrix))

# Print the sum of all elements
print("\nSum of all elements:", np.sum(matrix))

# Print the mean of all elements
print("Mean:", np.mean(matrix))

# Print the standard deviation
print("Standard Deviation:", np.std(matrix))

# Print the sum of each row
print("\nSum of each row:")
print(np.sum(matrix, axis=1))

# Print the sum of each column
print("\nSum of each column:")
print(np.sum(matrix, axis=0))