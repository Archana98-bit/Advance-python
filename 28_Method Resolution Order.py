# Method Resolution Order(MRO) Algorithm :
# a)
class A : pass
class B(A) : pass
class C(A) : pass
class D(B) : pass
class E(C) : pass
class F(D,E) : pass

print(A.__mro__)

print(B.__mro__)

print(C.__mro__)

print(D.__mro__)

print(E.__mro__)

print(F.__mro__)


# b)
class A :
    def m1(self) :
        print('A class m1 method')

class B(A) :
    def m1(self) :
        print('B class m1 method')

class C(A) :
    def m1(self) :
        print('C class m1 method')

class D(B) :
    def m1(self) :
        print('D class method')

class E(C) :
    def m1(self) :
        print('E class method')

class F(D,E) :
    pass

f = F()
f.m1()


# c)
class A :
    def m1(self) :
        print('A class m1 method')

class B(A) :
    def m1(self) :
        print('B class m1 method')

class C(A) :
    def m1(self) :
        print('C class m1 method')

class D(B) :
    def m1(self) :
        print('D class method')

class E(C) :
    def m1(self) :
        print('E class method')

class F(D,E) :
    def m1(self) :
        print('F class method')

f = F()
f.m1()



# d)
class A :
    pass

class B(A) :
    pass

class C(A) :
    pass

class D(B) :
    pass

class E(C) :
    pass

class F(D,E) :
    pass

f = F()
f.m1()   #F' object has no attribute 'm1'



# e)
class A : pass
class B : pass
class C(A) : pass
class D(A) : pass
class F(B) : pass
class G(B) : pass
class E(C,D,F) : pass

print(E.__mro__)

