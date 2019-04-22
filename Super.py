class A:
     def m1(self):
        print("Inside A m1")

class B(A):
    def m1(self):
        print("Inside B m1")

class C(B):
    def m1(self):
        print("Inside C m1")
class D(C):
    def m1(self):
        print("Inside D m1")
class E(D):
    def m1(self):
        super(C,self).m1()

e = E()
e.m1()
