import sympy as sp
import numpy as np
from sympy.functions import sin, cos, exp
import matplotlib.pyplot as plt

x = sp.Symbol('x')
f = sin(x)

print(f.diff(x, 3))


def TaylorSeries(func, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (func.diff(x, i).subs(x, x0)) / sp.factorial(i) * (x - x0) ** i
        i += 1
    return p


def showTatlorSeries():
    xx = np.linspace(-10, 10, 100)
    y = []

    for k in range(1, 8, 2):
        func = TaylorSeries(f, 0, k)
        for j in xx:
            y.append(func.subs(x, j))
        plt.plot(xx, y, label='order' + str(k))
        y = []
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


showTatlorSeries()
