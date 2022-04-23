import numpy as np


def GaussElimination(A, b):
    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i, k] != 0:
                lmbd = A[i, k] / A[k, k]
                A[i, :] = A[i, :] - lmbd * A[k, :]
                b[i] = b[i] - lmbd * b[k]
    return A, b


def GaussSubs(A, b):
    n = len(A)
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - A[k, k + 1:n] * b[k + 1:n]) / A[k, k]

    return b


A = np.matrix([[4.0, -2.0, 1.0], [-2.0, 4.0, -2.0], [1.0, -2.0, 4.0]])
b = np.matrix([11.0, -16.0, 17.0])

# aa, bb = GaussElimination(A, b.T)
# xx = GaussSubs(aa, bb)
#
# print(xx)
from numpy.linalg import inv
xSol = inv(A)*b.T
print(xSol)

