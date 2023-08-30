# Static variable deletion in various places :

# 1) outside of the class(usung class name) :
class Student :
    college = "XYZ"   #static variable
    principal = "Priyanka"  #static variable

print(Student.__dict__)

del Student.principal   #delete principal variable
print("\n After deletion \n")
print(Student.__dict__)


# 2) inside constructor :
# a)
class Student :
    college = "DTU"
    course = "MCA"

    def __init__(self) :
        del Student.college

print(Student.__dict__)
s1 = Student()
print("\n after deletion \n")
print(Student.__dict__)


# b)
class Student :
    college = "DTU"
    course = "MCA"

    def __init__(self) :
        del Student.college, Student.course    #delete multiple variables

print(Student.__dict__)
s1 = Student()
print("\n after deletion \n")
print(Student.__dict__)


# 3) inside instance method :
class Student :
    college = "DCE"
    hod = "DR. Rahul"

    def dlt(self) :
        del Student.college

print(Student.__dict__)
s1 = Student()
s1.dlt()
print("\n after deletion \n")
print(Student.__dict__)


# 4) inside class method(using class name) :
class Student :
    college = "DCE"
    principal = "Dr. Tushar"
    @classmethod
    def cm(cls) :
        del Student.college

print(Student.__dict__)
Student.cm()
print("\n after deletion \n")
print(Student.__dict__)


# b) using cls variable :
class Student :
    college = "DCE"
    principal = "Dr. Tushar"
    @classmethod
    def cm(cls) :
        del cls.college

print(Student.__dict__)
Student.cm()
print("\n after deletion \n")
print(Student.__dict__)


# 5) inside static method(using class name) :
class Student :
    college = "MNT"
    principal = "Dr. Tushar"
    @staticmethod
    def sm() :
        del Student.college

print(Student.__dict__)
s1 = Student()
s1.sm()
print("\n after deletion \n")
print(Student.__dict__)

