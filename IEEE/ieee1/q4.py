import numpy as np

x = np.random.random((3, 3))
print(x)

# creating a numpy array of integers
arr = np.array(x)

# finding the maximum and
# minimum element in the array
max_element = np.max(arr)
min_element = np.min(arr)

# printing the result
print('maximum element in the array is: ',
      max_element)
print('minimum element in the array is: ',
      min_element)
