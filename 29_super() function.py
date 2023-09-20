# super() function :
# a) problem without super function :
class Employee :
    def __init__(self, name, age, eid, sal) :
        self.name = name
        self.age = age
        self.eid = eid
        self.sal = sal

    def printDetails(self) :
        print(f'Employee Name : {self.name}')
        print(f'Employee Age : {self.age}')
        print(f'Employee ID : {self.eid}')
        print(f'Employee Salary : {self.sal}')
        print('-'*20)

class Student :
    def __init__(self, name, age, sid, course, college) :
        self.name = name
        self.age = age
        self.sid = sid
        self.course = course
        self.college = college

    def printDetails(self) :
        print(f'Student Name : {self.name}')
        print(f'Student age : {self.age}')
        print(f'Student ID : {self.sid}')
        print(f'Course : {self.course}')
        print(f'College : {self.college}')
        print('-'*20)

class Faculty :
    def __init__(self, name, age, fid, dept, college) :
        self.name = name
        self.age = age
        self.fid = fid
        self.dept = dept
        self.college = college

    def printDetails(self) :
        print(f'Faculty Name : {self.name}')
        print(f'Faculty Age : {self.age}')
        print(f'Faculty ID : {self.fid}')
        print(f'Dept : {self.dept}')
        print(f'College : {self.college}')

e = Employee('Rahul', 27, 1024, 10000)
e.printDetails()

s = Student('Priyanka', 23, 1011, 'MCA', 'CEB')
s.printDetails()

f = Faculty('Dr. Chand', 28, 1022, 'CSE', 'CEB')
f.printDetails()



# Solution by using super function :
class Human :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetails(self, name, age) :
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')

class Employee(Human) :
    def __init__(self, name, age, eid, sal) :
        super().__init__(name, age)
        self.eid = eid
        self.sal = sal

    def printDetails(self) :
        super().printDetails()
        print(f'Employee ID : {self.eid}')
        print(f'Salary : {self.sal}')
        print('-'*20)

class Student(Human) :
    def __init__(self, name, age, sid, course, college) :
        super().__init__(name, age)
        self.sid = sid
        self.course = course
        self.college = college

    def printDetails(self):
        super().printDetails()
        print(f'Student ID : {self.sid}')
        print(f'Course : {self.course}')
        print(f'College : {self.college}')
        print('-'*20)

class Faculty(Human) :
    def __init__(self, name, age, fid, dept, college) :
        super().__init__(name, age)
        self.fid = fid
        self.dept = dept
        self.college = college

    def printDetails(self):
        super().printDetails()
        print(f'Faculty ID : {self.fid}')
        print(f'Dept : {self.dept}')
        print(f'College : {self.college}')

e = Employee('Jack', 29, 1024, 15000)
e.printDetails()

s = Student('Archana', 24, 1022, 'MBA', 'DTU')
s.printDetails()

f = Faculty('Dr. Suresh', 31, 11234, 'EEE', 'DCE')
f.printDetails()

