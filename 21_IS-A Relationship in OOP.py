# IS-A Relationship in OOP :
# a)
class A :
    def method1(self) :
        print('A class method1')

    def method2(self) :
        print('A class method2')
    
    def method3(self) :
        print('A class method3')

class B :
    def method4(self) :
        print('B class method4')

b = B()
b.method4()
#b.method1()   #'B' object has no attribute 'method1'


# b)
class A :
    def method1(self) :
        print('A class method1')

    def method2(self) :
        print('A class method2')
    
    def method3(self) :
        print('A class method3')

class B(A):
    def method4(self) :
        print('B class method4')

b = B()
b.method4()
b.method1()
b.method2()
b.method3()



# c) With Inheritance :
class A :
    def __init__(self) :
        self.x = 100
        self.y = 200

class B(A) :
    def printDetails(self) :
        print(f'x : {self.x}')
        print(f'y : {self.y}')

b = B()
b.printDetails()



# d) Without Inheritance :
class A :
    def __init__(self) :
        self.x = 100
        self.y = 200

class B :
    def __init__(self) :
        self.x = 100
        self.y = 200

    def printDetails(self) :
        print(f'x is {self.x}')
        print(f'y is {self.y}')

b = B()
b.printDetails()



# e)
class Employee :
    def __init__(self, ename, eid, eaddress) :
        self.ename = ename
        self.eid = eid
        self.eaddress = eaddress

class Person(Employee) :
    def printDetails(self) :
        print(f'Employee Name : {self.ename}')
        print(f'Employee ID : {self.eid}')
        print(f'Employee Address : {self.eaddress}')

p = Person('Priyanka', 1011, 'Cuttack')
p.printDetails()

