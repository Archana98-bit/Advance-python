# Constructor :

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

    def printDetails(self) :
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Roll : {self.roll}')

s = Student('Priyanka', 24, 1024)
s.printDetails()



# b) Constructor will execute only once per object
class Employee :
    def __init__(self, name, age, eid) :
        self.name = name
        self.age = age
        self.eid = eid

    def printDetails(self) :
        print(f'Name : {self.name}')
        print(f'Age : {self.name}')
        print(f'Employee ID : {self.eid}')

e = Employee('Rahul', 27, 12345)
e.printDetails()
e.printDetails()
e.printDetails()



# c)
class Faculty() :
    def __init__(self, name, age, sal) :
        self.name = name
        self.age = age
        self.sal = sal

    def printDetails(self) :
        print('-'*20)
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Salary : {self.sal}')

f1 = Faculty('Dr. Chand', 30, 20000)
f1.printDetails()

f2 = Faculty('Dr. Suresh', 31, 70000)
f2.printDetails()
print('-'*20)



# d) Define a class without constructor :
class Employee :
    def companyName(self) :      #Here we did not create any constructor but python will add one default constructor behind the screen.
        print('Company Name is ABC pvt.ltd.')

e = Employee()
e.companyName()

print('-'*20)

# e) If we will call the constructor manually then python will treat it as a normal method call.

class Computer :
    def __init__(self) :
        print('This is a Computer')

c1 = Computer()  # Constructor will execute automatically
c1.__init__()    # Python will treat __init__(self) as a normal python method
c1.__init__()
c1.__init__()

print('-'*20)

# f)
class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

    def printDetails(self) :
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Roll : {self.roll}')

s1 = Student('Priyanka', 23, 112233)
s1.printDetails()

s1.__init__('Rahul', 24, 1025)
s1.printDetails()

print('-'*20)

# g) We can not create multiple constructor a single class :
class Laptop :
    def __init__(self, lname, date) :
        self.lname = lname
        self.date = date

    def __init__(self, price) :
        self.price = price

    def printDetails(self) :
        print(f'Laptop Name : {self.lname}')
        print(f'Laptop Date : {self.date}')
        print(f'Laptop Price : {self.price}')

l1 = Laptop('HP', 17-8-2012, 485000)
l1.printDetails()

l1.__init__('Dell', 20-3-2023, 50000)
l1.printDetails()


# Types of Constructor :
# Non-Parameterize Constructor :
class Employee :
    def __init__(self) :
        print('Here is a constructor')

e1 = Employee()



# Parameterized Constructor :
class College :
    def __init__(self, name, area) :
        self.name = name
        self.area = area

c1 = College('DTU', 'BBSR')



# Default Constructor :
class Faculty :
    def facultyName(self) :
        print('Faculty Name is Dr. Arun Tripathy')

f1 = Faculty()
f1.facultyName()

