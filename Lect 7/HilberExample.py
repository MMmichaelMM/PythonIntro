import numpy as np
from scipy.linalg import hilbert
from numpy.linalg import inv

H1 = hilbert(5)
b = np.ones((5, 1), dtype=float)
print(b)
x1 = inv(H1)@b
print(x1)

H2 = H1
H2[4, 4] = H2[4, 4] * 1.01
x2 = inv(H2)@b
print(x2)