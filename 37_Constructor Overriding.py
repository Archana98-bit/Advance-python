# Constructor Overriding :
# a)
class Parent :
    def __init__(self) :
        print('Hello! I like Python')

class Child(Parent) :
    pass

c = Child()


print('-'*20)


# b)
class Parent :
    def __init__(self) :
        print('Hello! I like Python')

class Child(Parent) :
    def __init__(self) :
        print('Hello! I like Java')

c = Child()


print('-'*20)



# c) Problem without using constructor overriding :
class Human :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def printDetails(self) :
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')


class Student(Human) :
    def __init__(self, name, age, roll, course, college) :
        self.name = name
        self.age = age
        self.roll = roll
        self.course = course
        self.college = college

    def printDetails(self):
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Roll number : {self.roll}')
        print(f'Course : {self.course}')
        print(f'College : {self.college}')

class Faculty(Human) :
    def __init__(self, name, age, fid, sal, college) :
        self.name = name
        self.age = age
        self.fid = fid
        self.sal = sal
        self.college = college

    def printDetails(self):
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Faculty ID : {self.fid}')
        print(f'Salary : {self.sal}')
        print(f'College : {self.college}')







# d) with using constructor overriding :
class Human :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def printDetails(self) :
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')


class Student(Human) :
    def __init__(self, name, age, roll, course, college) :
        super().__init__(name, age)   # calling parent class constructor
        self.roll = roll
        self.course = course
        self.college = college

    def printDetails(self):
        super().printDetails()
        print(f'Roll number : {self.roll}')
        print(f'Course : {self.course}')
        print(f'College : {self.college}')

class Faculty(Human) :
    def __init__(self, name, age, fid, sal, college) :
        super().__init__(name, age)
        self.fid = fid
        self.sal = sal
        self.college = college

    def printDetails(self):
        super().printDetails()
        print(f'Faculty ID : {self.fid}')
        print(f'Salary : {self.sal}')
        print(f'College : {self.college}')


f = Faculty('Dr. Chand', 30, 12345, 20000, 'CEB college')
f.printDetails()


s = Student('Rahul', 24, 101, 'MCA', 'DCE')
s.printDetails()


print('-'*20)

