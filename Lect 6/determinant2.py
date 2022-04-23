import numpy as np


def determinantLU(M):
    n = len(M)
    if n == 1:
        d = M[0, 0]
    else:
        u11 = M[0, 0]                         # u11 = a11
        U12 = np.matrix(M[0, 1:])             # U12 = A12
        L21 = np.matrix((1 / u11) * M[1:, 0]) # L21 = (1 / u11) * A21
        d = u11 * determinantLU(M[1:, 1:] - L21.T * U12)
    return d

C = np.random.randint(1, 10, size=(3, 3))
print(C)
print(determinantLU(C))
print(np.linalg.det(C))