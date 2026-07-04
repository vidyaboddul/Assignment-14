# Q1. Array Properties

# Import NumPy library
import numpy as np

# Create a 2D array of shape (5, 6) with random integers from 10 to 100
array = np.random.randint(10, 101, (5, 6))

# Display the array
print("2D Array:")
print(array)

# Print the shape of the array
print("\nShape of the array:", array.shape)

# Print the total number of elements
print("Total number of elements (size):", array.size)

# Print the data type of the array
print("Data type (dtype):", array.dtype)