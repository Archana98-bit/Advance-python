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


# Accessing and Deleting of instance variable.
# 1) accessing instance variable :

# access within the class :
# a)

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

    #accessing instance variable within the class inside a instance method.
    def printDetails(self) :
        print(f'name is {self.name}')
        print(f'age is {self.age}')
        print(f'roll is {self.roll}')

s1 = Student('priyanka', 24, 1024)
s1.printDetails()


# b)

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

        #accessing instance variable inside the class present inside the constructor.
        print(f'name is {self.name}')
        print(f'age is {self.age}')
        print(f'roll is {self.roll}')

s1 = Student('priyanka', 24, 1026)


# access inside variable outside of the class :
# a)
class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll
s1 = Student('Zini', 23, 1023)
#accesing instance variable outside of the class using object referance
print(f'name is {s1.name}')
print(f'age is {s1.age}')
print(f'roll is {s1.roll}')



# b)
class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll
s1 = Student('Zini', 23, 1023)
#accesing instance variable outside of the class using object referance
print(f'name is {s1.name}')
print(f'age is {s1.age}')
print(f'roll is {s1.roll}')

s2 = Student('Jack', 25, 1025)
print(f'name is {s2.name}')
print(f'age is {s2.age}')
print(f'roll is {s2.roll}')


# Deletion of instance variable.
# delete from inside the class :

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll
    #delete instance variable inside a class present inside instance method.
    def deleteData(self) :
        del self.name
        del self.roll

s1 = Student('Anjali', 25, 1026)
print(s1.__dict__)
s1.deleteData()

print(s1.__dict__)


# delete instance variable inside the class inside the constructor.

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll
        print(self.__dict__)   #it will give details of instance variable
        #delete instance variable inside class inside a constructor
        del self.name

s1 =Student('Rashmi', 22, 1027)
print(s1.__dict__)


# Deletion of instance variable outside of class

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

s1 = Student('Archana', 25, 1024)
print(s1.__dict__)
#delete instance variable outside of the class using referance variable.
del s1.age, s1.roll
print(s1.__dict__)
