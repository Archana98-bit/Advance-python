# Creation of multiple objects from a single class :

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

    def printDetails(self) :
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Roll is {self.roll}')
        print('-'*20)

s1 = Student('Priyanka', 24, 1024)
s1.printDetails()

s2 = Student('Rahul', 25, 1025)
s2.printDetails()

s3 = Student('Zini', 23, 1026)
s3.printDetails()

s4 = Student('Jack', 24, 1027)
s4.printDetails()


# Creating multiple objects from a single class using (list / loop) :

class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

    def printDetails(self) :
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(f'Roll is {self.roll}')
        print('-'*20)

names = ['Priyanka', 'Rahul', 'Zini', 'Jack', 'Dev', 'Anjali', 'Archana', 'Dr. Chand', 'Scoot']
age = [23, 24, 25, 23, 24, 25, 24, 23, 22]
roll = [1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032]

obj_list = []

for i in range(len(names)) :
    s = Student(names[i], age[i], roll[i])
    obj_list.append(s)

print(obj_list)

print(obj_list[0])

print(obj_list[0].name)
print(obj_list[0].age)
print(obj_list[0].roll)


print(obj_list[1].name)
print(obj_list[1].age)
print(obj_list[1].roll)

print(obj_list[2].name)
print(obj_list[2].age)
print(obj_list[2].roll)

# or,
for i in range(len(names)) :
    print(obj_list[i].name)
    print(obj_list[i].age)
    print(obj_list[i].roll)
    print('-'*20)
    

