import numpy as np

# create NumPy array of floats
float_array = np.array([12.3, 14.5, 11.1, 9.9, 12.2, 8.2])

float_array1 = np.float32(float_array)

# view array
print(float_array1)

# view dtype of array
print(float_array1.dtype)

# convert NumPy array of floats to array of integers (rounded to nearest)
rounded_integer_array = (np.rint(float_array1)).astype(int)

# view array
print(rounded_integer_array)

# view dtype of array
print(rounded_integer_array.dtype)
