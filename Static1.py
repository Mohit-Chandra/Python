class Test:

    a=10
    def __init__(self):
        self.b = 20
        Test.x = 10
    
    def m1(self):
        Test.b = 30
    
    @classmethod
    def m2(cls):
        Test.c=40
        cls.d=50

    @staticmethod
    def m3():
        Test.e = 10

print(Test.__dict__)
t=Test()
t.a = 20
Test.a = Test.a+20
print(Test.a)
print(t.a)
t.m1()
Test.m2()
Test.m3()
print(Test.__dict__)