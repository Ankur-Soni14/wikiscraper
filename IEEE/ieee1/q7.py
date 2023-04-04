# 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
import numpy as np

Z = np.arange(3)
Z ** Z       # = [0^0, 1^1, 2^2] = [1, 1, 4]
2 << Z >> 2  # = [0, 1, 2]
Z < - Z      # = [False, False, False]
1j * Z       # = [0 + 0.j, 0 + 1.j, 0 + 2.j]
Z / 1 / 1    # = [0, 1, 2]
Z < Z > Z    # ValueError
