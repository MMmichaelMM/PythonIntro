class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


e = MyClass(8, 6)
print(e.add())