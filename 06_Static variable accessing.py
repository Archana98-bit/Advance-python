# Static variable accessing in different places :

# 1) outside of the class :
class Student :
    college = "DCE"     #static variable

print(Student.college)


# 2) inside constructor :
class Student :
    college = "DTU"

    def __init__(self) :
        print(Student.college)

s1 = Student()


# 3) inside instance method :
class Student :
    college = "BHU"

    def display(self) :
        print(Student.college)

s1 = Student()
s1.display()


# 4) inside class method(using class name) :
# a)
class Student :
    college = "CEB"
    @classmethod
    def cm(cls) :
        print(Student.college)  #accessing static variable using class name

Student.cm()


# b) using cls variable :
class Student :
    college = "XYZ"
    @classmethod
    def cm(cls) :
        print(cls.college)  #accessing static variable using class name

Student.cm()


# 5) inside static method :
class Student :
    college = "MNO"
    @staticmethod
    def sm() :
        print(Student.college)

s1 = Student()
s1.sm()


print(Student.__dict__)

print(s1.__dict__)


