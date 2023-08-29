# Modify Static variable value :

# 1) outside of the class :
class Student :
    college = "CEB"  #static variable

print(Student.college)   #before modification

Student.college = "DCE"
print(Student.college)


# 2) inside constructor :
class Student :
    college = "DCE"

    def __init__(self) :
        Student.college = "DTU"

print(Student.college)

s1 = Student()  #after modification
print(Student.college)


# 3) inside instance method :
class Student :
    college = "COE"

    def modify(self) :
        Student.college = "BHU"

print(Student.college)
s1 = Student()

s1.modify()
print(Student.college)


# 4) inside class method(using class name) :
# a)
class Student :
    college = "DTU"

    @classmethod
    def cm(cls) :
        Student.college = "CEB"  #modify

print(Student.college)

s1 = Student()
s1.cm()
print(Student.college)


# b) using cls variable :
class Student :
    college = "DTU"

    @classmethod
    def cm(cls) :
        cls.college = "STV"  #modify

print(Student.college)

s1 = Student()
s1.cm()
print(Student.college)



# 5) inside static method :
class Student :
    college = "MNT"

    @staticmethod
    def sm() :
        Student.college = "OPT"

print(Student.college)

s1 = Student()
s1.sm()
print(Student.college)


# Modifying static variable values using self / object referance :
# a) modify using self(unexpected result) :
class Student :
    college = "XYZ"

    def __init__(self) :
        self.college = "MNT"  # it will create instance variable instead of modifying static variables

print(Student.college)
s1 = Student()
print(Student.college)

print(Student.__dict__)

print(s1.__dict__)


# b) using object referance variable :
class Student :
    college = "XYZ"

s1 = Student()
print(Student.college)
s1.college = "COEB"  # it will create instance variable for s1 object
print(Student.college)

print(s1.__dict__)


