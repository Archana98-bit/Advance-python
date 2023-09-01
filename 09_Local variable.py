# Local variable :
# a)
class Calculation :
    def add(self) :
        a = 23
        b = 33
        result = a+b
        print(result)

c1 = Calculation()
c1.add()


# b)
class Calculation() :
    def test(self) :
        a = 22
        b = 66
        print(a)
        print(b)
    
    def demo(self) :
        print(a)
        print(b)

c1 = Calculation()
c1.test()


# c)
class Calculation() :
    def test(self) :
        a = 100
        b = 200
        print(a)
        print(b)
        del a
        #print(a)   #localerror

c1 = Calculation()
c1.test()


# d)
class Student :
    def __init__(self, name, age, roll) :
        self.name = name
        self.age = age
        self.roll = roll

    def printDetails(self) :
        print(self.name)   #accessing instance variable
        #print(name)  #accessing local variable ,  #nameError

s1 = Student('Rahul', 24, 1024)
s1.printDetails()


# e)
class Student :
    def __init__(self, n, a, r) :
        self.name = n
        self.age = a
        self.roll = r

    def printDetails(self) :
        print(self.name)   #accessing instance variable
        #print(n)  #accessing local variable ,  #nameError

s1 = Student('Rahul', 24, 1024)
s1.printDetails()

