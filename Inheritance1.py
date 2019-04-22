class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
    
    def getInfo(self):
        print('\t Car Name:{}\t Car Model: {}\tCar Color{}: '.format(self.name,self.model,self.color))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def eat_n_drink(self):
        print('Eat kofta and drink water')
    
   
 
class Employee(Person):

     def __init__(self,name,age,eno,esal,car):
         super().__init__(name,age)
         self.eno = eno
         self.esal=esal
         self.car= car

     def work(self):
         print('Coding Java')
    
     def empInfo(self):
        print('Employee Name: ',self.name)
        print('Employee Age: ',self.age)
        print('Employee Eno: ',self.eno)
        print('Employee Sal: ',self.esal)
        print('Car Info: ')
        self.car.getInfo()
     def m1(self):
        print('Inside Employee m1')

c = Car('Maruti','M800','Red')
e = Employee('Mohit',28,1294044,80000,c)
p = Person("Mohit",19)
e.m1()
e.empInfo()


    