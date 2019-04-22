class A:
    pass

class B:
    def m1(self):
        print("Inside B m1")

class C:
    def m1(self):
        print("Inside C m1")

class X(A,B):
    pass

class Y(B,C):
    def m1(self):
        print("Inside Y m1")

class P(X,Y,C):
    pass
  
p=P()
p.m1()
print(P.mro())

