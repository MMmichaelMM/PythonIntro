import numpy as np
from numpy import pi, cos, sin
from numpy.linalg import pinv
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

N = 50
R = np.random.uniform(10, 16,size=N)
alpha = np.linspace(0, 2*pi, N)

x = 10+R*cos(alpha)
y = 1+R*sin(alpha)

# Formulation of Ax=b
A = np.zeros((N, 3))
b = np.zeros((N, 1))

A[:, 0] = x
A[:, 1] = y
A[:, 2] = 1

b[:, 0] = x**2 + y**2
X = np.dot(pinv(A), b)

print(X)

aa = X[0]/2
bb = X[1]/2
RR = np.sqrt(X[2]+aa**2+bb**2)

x_fit = aa+RR*cos(alpha)
y_fit = bb+RR*sin(alpha)

plt.figure()
plot(x, y,'.b', x_fit, y_fit, 'r', linewidth=3)
plt.show()




