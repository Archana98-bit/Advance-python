# Operator Overloading :

# a) Operator overloading without magic method (which is not possible):
class Employee :
    def __init__(self, sal) :
        self.sal = sal

class Student :
    def __init__(self, pkt_money) :
        self.pkt_money = pkt_money

e = Employee(10000)
s = Student(500)

# print(e+s)     #unsupported operand type(s) for +: 'Employee' and 'Student'



# b) Operator overloading with using magic method :
class Employee :
    def __init__(self, sal) :
        self.sal = sal

    def __add__(self, other) :    #magic method which is automatically call by python
        return self.sal + other.pkt_money

class Student :
    def __init__(self, pkt_money) :
        self.pkt_money = pkt_money

e = Employee(10000)
s = Student(500)

# add emp sal + student pkt_money
print(e+s)

print('-'*20)

# c)
class Employee :
    def __init__(self, sal) :
        self.sal = sal

    def __add__(self, other) :
        print(self.sal)
        print(other.pkt_money)
        return self.sal + other.pkt_money

class Student :
    def __init__(self, pkt_money) :
        self.pkt_money = pkt_money

e = Employee(10000)
s = Student(500)

# add emp sal + student pkt_money
print(e+s)


print('-'*20)

# d) __gt__() method :
class Employee :
    def __init__(self, sal) :
        self.sal = sal

    def __gt__(self, other) :     # magic method
        print(self.sal)
        print(other.pkt_money)
        return self.sal > other.pkt_money

class Student :
    def __init__(self, pkt_money) :
        self.pkt_money = pkt_money

e = Employee(10000)
s = Student(500)

# check which is greater emp sal, student pkt_money
print(e>s)


print('-'*20)




# e) __lt__() method :
class Employee :
    def __init__(self, sal) :
        self.sal = sal

    def __lt__(self, other) :     # magic method
        print(self.sal)
        print(other.pkt_money)
        return self.sal < other.pkt_money

class Student :
    def __init__(self, pkt_money) :
        self.pkt_money = pkt_money

e = Employee(10000)
s = Student(500)

# check which is lesser emp sal, student pkt_money
print(e<s)


print('-'*20)



# f) __ge__() method :
class Employee :
    def __init__(self, sal) :
        self.sal = sal

    def __ge__(self, other) :     # magic method
        print(self.sal)
        print(other.pkt_money)
        return self.sal >= other.pkt_money

class Student :
    def __init__(self, pkt_money) :
        self.pkt_money = pkt_money

e = Employee(10000)
s = Student(10000)

# check which is greater than equall to emp sal, student pkt_money
print(e>=s)


print('-'*20)






# g) __le__() method :
class Employee :
    def __init__(self, sal) :
        self.sal = sal

    def __le__(self, other) :     # magic method
        print(self.sal)
        print(other.pkt_money)
        return self.sal <= other.pkt_money

class Student :
    def __init__(self, pkt_money) :
        self.pkt_money = pkt_money

e = Employee(10000)
s = Student(10000)

# check which is less than equall to emp sal, student pkt_money
print(e<=s)


print('-'*20)






# h)
class Employee :
    def __init__(self, sal) :
        self.sal = sal

    def __sub__(self, other) :     # magic method
        print(self.sal)
        print(other.pkt_money)
        return self.sal - other.pkt_money

class Student :
    def __init__(self, pkt_money) :
        self.pkt_money = pkt_money

e = Employee(10000)
s = Student(1000)

# substract from emp sal to student pkt_money
print(e-s)


print('-'*20)



# i)
class Employee :
    def __init__(self, sal) :
        self.sal = sal

    def __mul__(self, other) :     # magic method
        print(self.sal)
        print(other.pkt_money)
        return self.sal * other.pkt_money

class Student :
    def __init__(self, pkt_money) :
        self.pkt_money = pkt_money

e = Employee(120)
s = Student(50)

# multiply from emp sal to student pkt_money
print(e*s)

