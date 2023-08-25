# without static variable.
class Student :
    def __init__(self, name, age, roll, college) :
        self.name = name
        self.age = age
        self.roll = roll
        self.college = college

s1 = Student('Priyanka', 23, 1024, 'DCE')
s2 = Student('Rahul', 24, 1025, 'DCE')
s3 = Student('Zini', 25, 1026, 'DCE')

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)


# with static variable.

class Student :
    college = "DCE"     #static variable
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

s1 = Student('Priyanka', 23, 1024)
s2 = Student('Rahul', 25, 1025)
s3 = Student('Zini', 24, 1026)

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

print(Student.__dict__)
