class A:
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3

a = A()
print(a.a) # 1
print(a._b) # 2
print(a.__c) # AttributeError: 'A' object has no attribute '__c'