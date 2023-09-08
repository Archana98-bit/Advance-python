# Has-A Relationship :
# a)
class Car :
    def __init__(self, cname, ccolor, cprice) :
        self.cname = cname
        self.ccolor = ccolor
        self.cprice = cprice

    def printCarDetails(self) :
        print(f'Car Name : {self.cname}')
        print(f'Car Color : {self.ccolor}')
        print(f'Car Price : {self.cprice}')

class Employee :
    def __init__(self, ename, eid, eaddress) :
        self.ename = ename
        self.eid = eid
        self.eaddress = eaddress
        self.c = Car('Maruti', 'White', 12345000)   #object creation of Car class
    
    def printEmpDetails(self) :
        print(f'Employee Name : {self.ename}')
        print(f'Employee ID : {self.eid}')
        print(f'Employee Address : {self.eaddress}')
        self.c.printCarDetails()


e = Employee('Priyanka', 123, 'BBSR')
e.printEmpDetails()



# b)
class Car :
    def __init__(self, cname, ccolor, cprice) :
        self.cname = cname
        self.ccolor = ccolor
        self.cprice = cprice

    def printCarDetails(self) :
        print(f'Car Name : {self.cname}')
        print(f'Car Color : {self.ccolor}')
        print(f'Car Price : {self.cprice}')

class Laptop :
    def __init__(self, lname, lcolor, lprice) :
        self.lname = lname
        self.lcolor = lcolor
        self.lprice = lprice

    def printLapDetails(self) :
        print(f'Laptop Name : {self.lname}')
        print(f'Laptop Color : {self.lcolor}')
        print(f'Laptop Price : {self.lprice}')

class Employee :
    def __init__(self, ename, eid, eaddress) :
        self.ename = ename
        self.eid = eid
        self.eaddress = eaddress
        self.c = Car('Audi', 'Black', 14500000)   #object creation of Car class
        self.l = Laptop('Dell', 'Grey', 50000)   #object creation of Laptop class
    
    def printEmpDetails(self) :
        print(f'Employee Name : {self.ename}')
        print(f'Employee ID : {self.eid}')
        print(f'Employee Address : {self.eaddress}')
        self.c.printCarDetails()
        self.l.printLapDetails()


e = Employee('Rahul', 1024, 'Cuttack')
e.printEmpDetails()


# NOTE : Without existance of container object , there is no existance of contained object.
# Example : Here if Employee object will not exist, then there is no existance of car and laptop object.


# c)
class Dept :
    def __init__(self, dname, dhod, did) :
        self.dname = dname
        self.dhod = dhod
        self.did = did

    def printDeptDetails(self) :
        print(f'Dept Name : {self.dname}')
        print(f'Dept HOD : {self.dhod}')
        print(f'Dept ID : {self.did}')
        print('-'*20)

class Student :
    def __init__(self, sname, sid, saddress) :
        self.sname = sname
        self.sid = sid
        self.saddress = saddress
        self.d = Dept('MCA', 'DR. Chand', 1024)  #HAS-A relationship
        self.d1 = Dept('MBA', 'Dr. Sunil', 1123) #object creation of Dept class

    def printStudentDetails(self) :
        print(f'Student Name : {self.sname}')
        print(f'Student ID : {self.sid}')
        print(f'Student Address : {self.saddress}')
        self.d.printDeptDetails()
        self.d1.printDeptDetails()

s = Student('Archana', 11223, 'Kendrapara')
s1 = Student('Priyanka', 12346, 'Balasore')
s.printStudentDetails()
s1.printStudentDetails()

