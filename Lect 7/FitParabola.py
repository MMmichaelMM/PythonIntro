import numpy as np
from numpy.linalg import pinv
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

N = 100
a = np.random.uniform(-2, -1, size=N)
b = np.random.uniform(0, 1, size=N)
c = np.random.uniform(18, 22, size=N)
x = np.linspace(-2, 2, N)
y = a*x**2+b*x+c

# Formulation of Ax=b
A = np.zeros((N, 3))
b = np.zeros((N, 1))

A[:, 0] = x**2
A[:, 1] = x
A[:, 2] = 1

b[:, 0] = y
X = np.dot(pinv(A), b)

aa = X[0]
bb = X[1]
cc = X[2]

y_fit = aa*x**2+bb*x+cc

plt.figure()
plot(x, y, '.b', x, y_fit, 'r', linewidth=3)
plt.show()