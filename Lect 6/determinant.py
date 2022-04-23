import numpy as np

def determinantRecursion(M):
    n = len(M)
    if n == 1:
        d = M[0, 0]
    else:
        sign = 1
        d = 0
        for i in list(range(n)):
            L = np.hstack((M[1:, :i], M[1:, i + 1:]))
            d = d + sign * M[0, i] * determinantRecursion(L)
            sign = -sign
    return d


C = np.random.randint(1, 10, size=(4, 4))
print(C)
print(determinantRecursion(C))

print(np.linalg.det(C))

