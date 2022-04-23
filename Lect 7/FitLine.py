import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, figure
from numpy.linalg import pinv

# Example of LSQ - Fit line to COP
N = 50
rx = np.random.uniform(1, 2, N)
ry = np.random.uniform(1, 5, N)
x = np.linspace(0, 10, N)
x = x+rx
a = 1.6
b = 4.9

y = a*x+b+ry
A = np.zeros((N, 2))
B = np.zeros((N, 1))
A[:, 0] = x
A[:, 1] = 1
B[:, 0] = y
X = np.dot(pinv(A), B)
print(X)

y_a = X[0]*x + X[1]

figure()
plot(x, y, '.', x, y_a)
plt.show()