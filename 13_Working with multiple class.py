# Working with multiple class :
class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

    def printDetails(self) :
        print('Student Information')
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Roll is {self.roll}')
        print('-'*20)

class Faculty :
    def __init__(self, name, age, fid) :
        self.name = name
        self.age = age
        self.fid = fid

    def printDetails(self) :
        print('Faculty Information')
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Fid is {self.fid}')

s1 = Student('Priyanka', 23, 1024)
s1.printDetails()

f1 = Faculty('Tushar', 29, 12345)
f1.printDetails()

