class Diff:
    def __init__(self, f, h=1E-5):
        self.f, self.h = f, h


class Forward1(Diff):
   def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h


class Central2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)


class Central4(Diff):
   def __call__(self, x):
        f, h = self.f, self.h
        return (4./3)*(f(x+h) - f(x-h)) /(2*h) - \
        (1./3)*(f(x+2*h) - f(x-2*h))/(4*h)


from math import pi, sin, cos
h = [1.0/(2**i) for i in range(5)]
ref = cos(pi/4)
print('    h      Forward1     Central2     Central4')
for h_ in h:
    f1 = Forward1(sin, h_); c2 = Central2(sin, h_); c4 = Central4(sin, h_)
    e1 = abs(f1(pi/4)-ref)
    e2 = abs(c2(pi/4)-ref)
    e4 = abs(c4(pi/4)-ref)
    print('{0:1.8f} {1:1.10f} {2:1.10f} {3:1.10f}'. \
          format(h_, e1, e2, e4))
