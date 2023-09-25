# Mehod Overloading :
# 2 or more methods with same name but arguments are different :

class Test :
    def method1(self,a) :
        print(a)
    
    def method1(self,a,b) :
        print(a)
        print(b)

    def method1(self,a,b,c) :
        print(a)
        print(b)
        print(c)

t = Test()
# t.method1(100,200)   #TypeError: Test.method1() missing 1 required positional argument: 'c'
t.method1(100, 200, 300)



print('-'*20)


# How to archieve method overloading in python :
class Test :
    def method1(self, *a) :
        print(a)

t = Test()
t.method1(10)
t.method1(10, 20)
t.method1(10, 20, 30)
t.method1(10, 20, 30, 40)


print('-'*20)



# another way to archieve method overloading in python :
class Test :
    def method1(self, a=None , b=None) :
        print(a)
        print(b)

t = Test()
t.method1(100, 200)
t.method1(200)
t.method1()


print('-'*20)


# c)
class Test :
    def method1(self, a=None, b=None) :
        if a!=None and b!=None :
            print('You provided two value')

        else :
            print('You did not provided two values')

t = Test()
t.method1(100, 200)
t.method1(100)


print('-'*20)



# Method overloading using multipledispatch module :
# a)
from multipledispatch import dispatch

class Test :

    @dispatch(int, int)
    def add(a,b) :
        print(a+b)

    @dispatch(float, float)
    def add(a,b) :
        print(a+b)

    @dispatch(int, float)
    def add(a,b) :
        print(a+b)

t = Test()
t.add(100, 200)
t.add(25.6, 13.8)
t.add(12, 3.67)


print('-'*20)




# b)
class Test :
    
    @dispatch(int, int)
    def add(a,b) :
        print(a+b)

    @dispatch(float, float)
    def add(a,b) :
        print(a+b)

    @dispatch(int, float)
    def add(a,b) :
        print(a+b)

    @dispatch(int, int, float)
    def add(a, b, c) :
        print(a+b+c)

t = Test()
t.add(100, 200)
t.add(25.6, 13.8)
t.add(12, 3.67)
t.add(100, 200, 38.9)


print('-'*20)


# c)
class Test :
    
    @dispatch(int, int)
    def add(a,b) :
        print(a+b)

    @dispatch(float, float)
    def add(a,b) :
        print(a+b)

    @dispatch(int, float)
    def add(a,b) :
        print(a+b)

    @dispatch(int, int, int)
    def sub(a, b, c) :
        print(a-b-c)

t = Test()
t.add(100, 200)
t.add(25.6, 13.8)
t.add(12, 3.67)
t.sub(1000, 500, 50)


