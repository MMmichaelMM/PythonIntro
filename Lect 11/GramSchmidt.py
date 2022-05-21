import numpy as np
import sympy as sp
from sympy import *
from matplotlib.pyplot import plot, show, figure

x = sp.symbols('x')

def innerProd(v1, v2, a, b):
    return integrate(v1*v2, (x, a, b))

def normInnerProd(v1, a, b):
    return sp.sqrt(innerProd(v1, v1, a, b))

# for given set {x^0, x^1, x^2} find orthonormal basis, where the inner
# product is given in range [-1, 1]
a = -1
b = 1
v1 = 1
v2 = x
v3 = x**2
v4 = x**3
v5 = x**4

u1 = v1
w1 = u1/normInnerProd(u1, a, b)
print('u1=', u1)
print('w1=', w1)

u2 = v2 - innerProd(x, w1, a, b)*w1
w2 = u2/normInnerProd(u2, a, b)
print('u2=', u2)
print('w2=', w2)

u3 = v3 - innerProd(v3, w1, a, b)*w1 - innerProd(v3, w2, a, b)*w2
w3 = u3/normInnerProd(u3, a, b)
print('u3=', u3)
print('w3=', w3)

u4 = v4 - innerProd(v4, w1, a, b)*w1 - innerProd(v4, w2, a, b)*w2 - innerProd(v4, w3, a, b)*w3
w4 = u4/normInnerProd(u4, a, b)
print('u4=', u4)
print('w4=', w4)

u5 = v5 - innerProd(v5, w1, a, b)*w1 - innerProd(v5, w2, a, b)*w2 - innerProd(v5, w3, a, b)*w3 - innerProd(v5, w4, a, b)*w4
w5 = u5/normInnerProd(u5, a, b)
print('u5=', u5)
print('w5=', w5)

# find approximations
# example 1: exp(x) = a1*w1 + a2*w2
# f = sp.exp(x)
f = 1 - x**4
a1 = innerProd(f, w1, a, b)
a2 = innerProd(f, w2, a, b)
a3 = innerProd(f, w3, a, b)
a4 = innerProd(f, w4, a, b)

exp_approx1 = a1*w1 + a2*w2
print('exp_approx1=', exp_approx1)

exp_approx2 = a1*w1 + a2*w2 + a3*w3
print('exp_approx2=', exp_approx2)

exp_approx3 = a1*w1 + a2*w2 + a3*w3 + a4*w4
print('exp_approx3=', exp_approx3)

# create graph
xx = np.linspace(a, b, 100)
y_f = [f.subs(x, x0) for x0 in xx]

# sol 1
y_exp_apprx1 = [exp_approx1.subs(x, x0) for x0 in xx]
y_exp_apprx2 = [exp_approx2.subs(x, x0) for x0 in xx]
y_exp_apprx3 = [exp_approx3.subs(x, x0) for x0 in xx]

# sol 2
# for i in xx:
#     y_exp_apprx.append(exp_approx.subs(x, i))

figure()
plot(xx, y_f, 'r', xx, y_exp_apprx1, 'b', xx, y_exp_apprx2, 'g', xx, y_exp_apprx3, 'k')
show()

# show the error
err1 = normInnerProd(np.e**x - exp_approx1, a, b)
err2 = normInnerProd(np.e**x - exp_approx2, a, b)
err3 = normInnerProd(np.e**x - exp_approx3, a, b)
print('err1=', float(err1))
print('err2=', float(err2))
print('err3=', float(err3))

# example 2: f(x) = 1 - x^4 in [-1,1]

# example 3: g(x) = sqrt(2*x+3) in [0,2] (use transformation from [0,2] to [-1,1]