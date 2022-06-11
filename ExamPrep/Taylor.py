import math
import sympy as sp
import numpy as np
from sympy import series
import matplotlib.pyplot as plt

x = sp.Symbol('x')
f = sp.log(1+x)
print(series(f, x))
print(f.diff(x, 1))


def TaylorSeries(func, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (func.diff(x, i).subs(x, x0)) / sp.factorial(i) * (x - x0) ** i
        i += 1
    return p


s = TaylorSeries(f, 0, 5)
print(s)


def showTaylorSeries():
    xx = np.linspace(0, 0.5, 10)
    ff = []
    for i in xx:
        ff.append(math.log(1 + i))
    plt.plot(xx, ff, label='log(1+x)')

    y = []

    for k in [1, 3]:
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


showTaylorSeries()
