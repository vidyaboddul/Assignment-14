# Q2. Statistical Methods - Basic

# Import NumPy library
import numpy as np

# Generate a 1D array of 20 random integers between 1 and 50
array = np.random.randint(1, 51, 20)

# Display the array
print("Array:")
print(array)

# Print the minimum value and its index
print("\nMinimum value:", np.min(array))
print("Index of minimum value:", np.argmin(array))

# Print the maximum value and its index
print("\nMaximum value:", np.max(array))
print("Index of maximum value:", np.argmax(array))

# Print the sum of all elements
print("\nSum of all elements:", np.sum(array))

# Print the mean of the array
print("Mean:", np.mean(array))

# Print the standard deviation of the array
print("Standard Deviation:", np.std(array))