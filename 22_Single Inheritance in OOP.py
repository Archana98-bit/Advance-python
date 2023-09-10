# Types of Inheritance :
# 1) Single Inheritance
# 2) Multi-Level Inheritance

# 1) Single Inheritance :
# a)
class A :
    def method1(self) :
        self.x = 10
        self.y = 20
        print(self.x)
        print(self.y)
    
    def method2(self) :
        self.a = 30
        self.b = 40
        print(self.a)
        print(self.b)

class B(A) :
    pass

b = B()
b.method1()
b.method2()


# b) child class can access own members as well as parent class members.
class A :
    def method1(self) :
        self.x = 10
        self.y = 20
        print(self.x)
        print(self.y)
    
    def method2(self) :
        self.a = 30
        self.b = 40
        print(self.a)
        print(self.b)

class B(A) :
    def method3(self) :
        self.i = 100
        self.j = 200
        print(self.i)
        print(self.j)

b = B()
b.method1()
b.method2()
b.method3()



# c) parent class can access only own members not child class members :
class A :
    def method1(self) :
        self.x = 10
        self.y = 20
        print(self.x)
        print(self.y)
    
    def method2(self) :
        self.a = 30
        self.b = 40
        print(self.a)
        print(self.b)

class B(A) :
    def method3(self) :
        self.i = 100
        self.j = 200
        print(self.i)
        print(self.j)

a = A()
a.method1()
a.method2()



# d)
class A :
    def im(self) :
        print('Parent class instance method')

    @classmethod
    def cm(cls) :
        print('Parent class class method')

    @staticmethod
    def sm() :
        print('Parent class static method')

class B(A) :
    pass

b = B()
b.im()
b.cm()
b.sm()



# e)

class A :
    m = 999   #static variable
    def im(self) :
        self.a = 100   #instance variable
        print('Parent class instance method')

    @classmethod
    def cm(cls) :
        cls.c = 50    #class variable
        print('Parent class class method')

    @staticmethod
    def sm() :
        l = 70    #Local variable
        print('Parent class static method')

class B(A) :
    pass

b = B()
b.im()
b.cm()
b.sm()
print(b.a)
print(b.c)
#print(b.l)     # B object has no attribute l.
print(b.m)



# f)
class A :
    def im(self) :
        self.i = 1000

class B(A) :
    pass

a = A()
a.im()
print(a.i)

b = B()
b.im()
print(b.i)

#print(a.i is b.i)



# g) If we will do any modification in child class, it will not reflect to parent class
class A :
    def im1(self) :
        self.i = 1000

class B(A) :
    def im2(self) :
        self.i = 99   #inside child class updated i value

a = A()
a.im1()
print(a.i)

b = B()
b.im1()
b.im2()
print(b.i)


print(a.__dict__)
print(b.__dict__)
