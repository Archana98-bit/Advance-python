# create a class student having 3 attributes and 1 methods.
#1)
class Student :
    def __init__(self) :
        self.name = input("Enter your name : ")
        self.age = int(input("Enter your age : "))
        self.course = input("Enter your course : ")

    def printDetails(self) :
        print("-"*30)
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"course is {self.course}")

s1 = Student()
s1.printDetails()


#2)
class Student :
    def __init__(self) :
        self.name = input("Enter your name : ")
        self.age = int(input("Enter your age : "))
        self.course = input("Enter your course : ")

    def printDetails(self) :
        print("-"*30)
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"course is {self.course}")

s1 = Student()

s2 = Student()

s3 = Student()

s1.printDetails()
s2.printDetails()
s3.printDetails()


# 3) Here self and s1 pointing to same memory location.
class student :
    def __init__(self) :
     print(id(self))
s1 = Student()
print(id(s1))

print("-"*20)

s2 = Student()
print(id(s2))


# 4) self is not a keyword.
class Student :
    def __init__(x) :
        x.name = input("Enter your name : ")
        x.age = int(input("Enter your age : "))
        x.course = input("Enter your course : ")

    def printDetails(x) :
        print("-"*30)
        print(f"name is {x.name}")
        print(f"age is {x.age}")
        print(f"course is {x.course}")

s1 = Student()
s1.printDetails()
