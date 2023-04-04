import numpy as np

Z = np.random.random((10, 2))
X, Y = Z[:, 0], Z[:, 1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y, X)
print(R)
print(T)
