# creation of Instance variable :
# 1) creation of instance variable inside a constructor :

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll
s1 = Student('priyanka', 22, 1011)
print(s1.__dict__)


# 2) creation of instance variable inside a instance method.

class Student() :
    def create(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll
s2 = Student()
print(s2.__dict__)
s2.create('rahul', 24, 1024)
print(s2.__dict__)


# 3) creation of instance variable outside of the class.

class Student :
    def __init__(self, name) :
        self.name = name
s3 = Student('zini')
print(s3.__dict__)
s3.age = 25       # creation of instance variable outside of class using referance variable
print(s3.__dict__)
s3.roll = 1025
print(s3.__dict__)


# 4) Programms on instance variable :

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll
    
    def printDetails(self) :
        print(f'name is {self.name}')
        print(f'age is {self.age}')
        print(f'roll is {self.roll}')

s1 = Student('priyanka', 23, 1024)
s1.address = 'BBSR'
s2 = Student('rahul', 24, 1025)
s2.adrees = 'CTC'
s3 = Student('zini', 25, 1026)
s3.address = 'Nayagarh'
s4 = Student('jack', 24, 1027)
s4.address = 'Sonpur'

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
print(s4.__dict__)

