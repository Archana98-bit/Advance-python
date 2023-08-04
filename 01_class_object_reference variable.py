# create a class student

class Student :
    def __init__(self,name,age,sid):
        self.name = name
        self.age = age
        self.sid = sid

    def printDetails(self) :
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"sid is {self.sid}")

s1 = Student("priyanka", 23, 1000)    #create an object
s1.printDetails()                     #reference variable

s2 =Student("rahul", 24, 1001)
s2.printDetails()

s3 = Student("zini", 25, 1002)
s3.printDetails()
