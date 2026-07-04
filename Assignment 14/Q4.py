# Q4. Reshape

# Import NumPy library
import numpy as np

# Create a 1D array containing numbers from 1 to 24
array = np.arange(1, 25)

# Display the original array
print("Original 1D Array:")
print(array)
print("Shape:", array.shape)

# Reshape into 4 x 6
array_4x6 = array.reshape(4, 6)
print("\n4 x 6 Array:")
print(array_4x6)
print("Shape:", array_4x6.shape)

# Reshape into 3 x 8
array_3x8 = array.reshape(3, 8)
print("\n3 x 8 Array:")
print(array_3x8)
print("Shape:", array_3x8.shape)

# Reshape into 2 x 3 x 4 (3D Array)
array_3d = array.reshape(2, 3, 4)
print("\n2 x 3 x 4 (3D Array):")
print(array_3d)
print("Shape:", array_3d.shape)