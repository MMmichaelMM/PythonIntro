class Parent:
    def __init__(self, a):
        self.a = a

    def print_var(self):
        print("The value of this class's variables are:")
        print(self.a)


class Child(Parent):
    def __init__(self, a, b):
        Parent.__init__(self, a)
        self.b = b

    def print_var(self):
        Parent.print_var(self)
        print(self.b)