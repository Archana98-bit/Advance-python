# Cyclic Inheritance :
# a)
class A(A) :
    def method1(self) :
        print('A class method1')

a = A()


# b)
class X(Y) :
    def method1(self) :
        print('X class method1')

class Y(X) :
    def method2(self) :
        print('Y class method2')

x = X()
y = Y()


# c) Solution :
class X :
    def method1(self) :
        print('X class method1')

    def method2(self) :
        print('X class method2')

x = X()
