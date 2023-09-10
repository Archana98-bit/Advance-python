# Multiple Inheritance :

class A :
    def method1(self) :
        self.x = 899
        print('A class method1')

    def method2(self) :
        print('A class method2')
    
    def test(self) :
        print('This is test method from class A')

class B :
    def method3(self) :
        self.y = 100
        print('B class method3')

    def method4(self) :
        print('B class method4')

class C(A,B) :
    def method5(self) :
        print('C class method5')
    
    def method6(self) :
        print('C class method6')

c = C()
c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
c.method6()
print(c.x)
print(c.y)
c.test()



# b) Ambiguity problem :
class A :
    def method1(self) :
        print('A class method1')

class B :
    def method1(self) :
        print('B class method1')

class C(A,B) :   # Here A is the first parent and B is the second parent(based on priority)
    def method2(self) :
        print('C class method2')

c = C()
c.method1()



# c)
class A :
    def method1(self) :
        print('A class method1')

class B :
    def method1(self) :
        print('B class method1')

class C(B,A) :   # Here B is the first parent and A is the second parent(based on priority)
    def method2(self) :
        print('C class method2')

c = C()
c.method1()



# d)
class A :
    def method1(self) :
        print('A class method1')

class B :
    def method1(self) :
        print('B class method1')

class C(A,B) :
    def method1(self) :
        print('C class method1')

c = C()
c.method1()

