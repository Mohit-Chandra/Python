class P1:
    def m1(self):
        print('P1 method')

class P2:
    def m1(self):
        print('P2 method')

class C(P2,P1):
    def m3(self):
        print('Child method')

c= C()
c.m1()
c.m3()