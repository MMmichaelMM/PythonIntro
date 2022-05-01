class Forward1:
    def __init__(self, f, h=1E-5):
        self.f, self.h = f, h

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h


class Central2:
    def __init__(self, f, h=1E-5):
        self.f, self.h = f, h

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)


class Central4:
    def __init__(self, f, h=1E-5):
        self.f, self.h = f, h

    def __call__(self, x):
        f, h = self.f, self.h
        return (4./3)*(f(x+h) - f(x-h)) /(2*h) - \
        (1./3)*(f(x+2*h) - f(x-2*h))/(4*h)