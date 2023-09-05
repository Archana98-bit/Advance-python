# Passing members of one class to another class :
# a)
class Student :
    def __init__(self, name, age, roll, address) :
        self.name = name
        self.age = age
        self.roll = roll
        self.address = address
    
    def printDetails(self) :
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Roll is {self.roll}')
        print(f'Address is {self.address}')

class Normal :

    @staticmethod
    def modify(r) :
        r.address = 'Bhubaneswar'

s1 = Student('Priyanka', 23, 1024, 'ctc')
s1.printDetails()

Normal.modify(s1)
s1.printDetails()


# b)
class Faculty :
    def __init__(self, name, fid) :
        self.name = name
        self.fid = fid

    def printDetails(self) :
        print(f'Name is {self.name}')
        print(f'Fid is {self.fid}')

class Normal :

    @staticmethod
    def modify(s) :
        s.fid = 12345

f1 = Faculty('Dr. Chand', 113324)
f1.printDetails()

Normal.modify(f1)
f1.printDetails()


# c)
class A :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    
    def printDetails(self) :
        print(f'X is {self.x}')
        print(f'Y is {self.y}')

class B :
    @staticmethod
    def modify(r) :
        r.y = 999

a1 = A(100, 200)
a1.printDetails()

B.modify(a1)
a1.printDetails()


# c) Passing single member of a class to another class :
class Student :
    def __init__(self, name, age, roll, address) :
        self.name = name
        self.age = age
        self.roll = roll
        self.address = address
    
    def printDetails(self) :
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Roll is {self.roll}')
        print(f'Address is {self.address}')

class Normal :

    @staticmethod
    def printInfo(r) :
        print(r)

s1 = Student('Priyanka', 23, 1024, 'ctc')

Normal.printInfo(s1.address)


