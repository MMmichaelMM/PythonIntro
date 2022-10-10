import numpy as np

def CheckIfPrime(N):
    if (N <= 3):
        s=1
    else:
        n = range(2, N)
        rem = [N % x for x in n]
        if (np.prod(rem)!= 0):
            s = 1
        else:
            s = 0
    return s


print(CheckIfPrime(17))
print(CheckIfPrime(9))
print(CheckIfPrime(5))