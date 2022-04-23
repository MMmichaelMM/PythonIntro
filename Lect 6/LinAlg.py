import numpy as np
from scipy.linalg import hilbert

# -Define Pascal matrix
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)


def PascalMat(n):
    P = np.zeros((n, n), dtype=int)
    for i in range(0, n):
        for j in range(0, n):
            P[i, j] = factorial(i + j) / factorial(i) / factorial(j)


print('Pascal, n =', 5, 'is ')
print(PascalMat(5))

H = hilbert(5)
print('Hilbert, n =', 5, 'is ')
print(H)