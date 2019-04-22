class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        print(id(self))
    def display(self):
        print(self.name)
        print(self.roll)
        print(self.marks)
        self.grade()
    def grade(self):
        if(self.marks>80):
            print("Grade is: A")
        elif(self.marks>=60):
            print("Grade is:B")
        else:
            print("Grade is C")
s1 =  Student("Mohit",10,80)
s1.display()
print(s1)
print(id(s1))

