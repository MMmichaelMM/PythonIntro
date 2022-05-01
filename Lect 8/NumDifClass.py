class Derivative:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def eval(self, x):
        f, h = self.f, self.h  # make short forms
        return (f(x+h) - f(x))/h


from math import exp, sin, pi
def f(x):
    return exp(-x)*sin(4*pi*x)

dfdx = Derivative(f)
print(dfdx.eval(1.2))