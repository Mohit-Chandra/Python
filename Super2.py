class A:
    a = 10
    def __init__(self):
        self.b = 20

class B(A):
    a = 777
    def m1(self):
        print(super().a)
        print(self.b)
        print(self.a)

b = B()
b.m1()