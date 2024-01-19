# How to create a thread by using OOP approach :
# Create thread in object oriented approach :
from threading import *

# by using single thread

class Test:
    def method1(self):
        for i in range(5):
            print('surendra')

    def method2(self):
        for i in range(5):
            print('priyanka')

ob=Test()
ob.method1()
ob.method2()


# by using multithredaing :

class Test:
    def m1(self):
        for i in range(5):
            print('surendra')

    def m2(self):
        for i in range(5):
            print('priyanka')

ob=Test()

t1=Thread(target=ob.m1)
t1.start()
t2=Thread(target=ob.m2)
t2.start()


# Passing argument :

class Test:
    def m1(self,name):
        for i in range(5):
            print(name)

    def m2(self,name):
        for i in range(5):
            print(name)

ob=Test()

t1=Thread(target=ob.m1,args=('surendra',))
t1.start()
t2=Thread(target=ob.m2,args=('priyanka',))
t2.start()


