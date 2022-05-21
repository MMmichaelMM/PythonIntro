import sympy as sp
from sympy import *
x = sp.symbols('x')
print(type(x))

f = sp.sin(x)
print('f = ', f)
print('f\' = ', f.diff(x, 1))
print('f\'\' = ', f.diff(x, 2))
print('integral of f = ', integrate(f))

f = sp.exp(x) + 3*x**3
print('f = ', f)
print('f\' = ', f.diff(x, 1))
print('f\'\' = ', f.diff(x, 2))

print('integral of f = ', integrate(f))


g = exp(x)*sin(x**2)
print('g = ', g)
print('g\' = ', g.diff(x, 1))
print('g\' = ', simplify(g.diff(x, 1)))

h = exp(x)*(x - 1)**2
dh = simplify(h.diff(x, 1))
print('h = ', h)
print('h\' = ', h.diff(x, 1))
print('h\'(2) = ', simplify(h.diff(x, 1)).subs(x, 2))
print('h\'(2) = ', dh.subs(x, 2))



