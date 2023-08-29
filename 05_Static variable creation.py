# Static variable creation in various places.

# 1) inside a class directly :
# a)
class Student :
    college = "DCE"   #static variable / class level variable

s1 = Student()

print(s1.__dict__)
print(Student.__dict__)


# b) inside class but outside of constructor and method.
class Student() :
    college = "DCE"   #static variable / class level variable
    branch = "Computer Science and Engineering"
    def __init__(self, name, age, roll) :
        self.name = name
        self. age = age
        self.roll = roll

    def printDetails(self) :
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Roll is {self.roll}')
        print('-'*20)

s1 = Student('Priyanka', 23, 1024)
s1.printDetails()

s2 = Student('Zini', 24, 1025)
s2.printDetails()

s3 = Student('Jack', 25, 1026)
s3.printDetails()

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

print(Student.__dict__)


# 2) Outside of the class(by using class name) :
# a)
class Student :
    pass   #empty class

s1 = Student()
Student.college = "DTU"    #static variable / class level variable
Student.branch = "CSE"     #staic variable
print(s1.__dict__)

print(Student.__dict__)


# b)

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.age = age

s1 = Student('Priyanka', 24, 1024)
s2 = Student('Rahul', 26, 1025)
s1 = Student('Anjali', 23, 1026)

Student.college = "JNU"
Student.branch = "MCA"

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

print(Student.__dict__)
print(Student.__dict__)


# 3) inside the constructor(using class name) :
# a)
class Student :
    def __init__(self) :
        Student.college = "BHU"   #static variable

s1 = Student()
s2 = Student()

print(s1.__dict__)
print(s2.__dict__)

print(Student.__dict__)


# b)
class Student :
    def __init__(self, name) :
        Student.college = "BHU"   #static variable
        self.name = name



s1 = Student('Priyanka')
s2 = Student('Archana')

print(s1.__dict__)
print(s2.__dict__)

print(Student.__dict__)


# 4) inside instance method(using class method) :
# a)

class Student :
    def create(self) :
        Student.college = "DCE"  #staic variable

s1 = Student()
s1.create()
print(s1.__dict__)

print(Student.__dict__)


# b)
class Student :
    def create(self, name) :
        Student.college = "DCE"  #staic variable
        self.name = name

s1 = Student()
s1.create('Rahul')

print(s1.__dict__)

print(Student.__dict__)


# 5) inside class method(using class name or cls variable) :
# a)

class Student :
    @classmethod
    def cm(cls) :
        Student.college = "BHU"  #static variable

s1 = Student()
Student.cm()   #call to class method by using class name
print(s1.__dict__)

print(Student.__dict__)


# b) using cls variable :

class Student :
    @classmethod
    def cm(cls) :
        cls.college = "DTU"  #static variable
        print(id(cls))

s1 = Student()
Student.cm()   #call to class method by using class name

print(s1.__dict__)

print(Student.__dict__)

# cls and Student both are pointing to same object
print(id(Student))


# 6) inside static method(using class name) :

class Student :
    @staticmethod
    def sm() :
        Student.college = "DCE"

s1 = Student()
s1.sm()
print(s1.__dict__)

print(Student.__dict__)




