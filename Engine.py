class Engine:
    a=10
    def __init__(self):
        self.b = 20
    def m1(self):
        print('Engine specific functionality')

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def m2(self):
        print('Class car using Engine functionality')
        print(Engine.a)
        print(self.engine.b)
        self.engine.m1()

c = Car()
c.m2()