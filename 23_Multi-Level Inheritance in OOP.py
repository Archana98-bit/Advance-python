# Multi-level Inheritance :

class A :
    def method1(self) :
        print('-'*20)
        print('Parent class method1')

    def method2(self) :
        print('Parent class method2')

class B(A) :
    def method3(self) :
        print('Child class method3')
    
    def method4(self) :
        print('Child class method4')

class C(B) :
    def method5(self) :
        print('Grandchild class method5')
    
    def method6(self) :
        print('Grandchild class method6')

c = C()
c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
c.method6()

b = B()
b.method1()
b.method2()
b.method3()
b.method4()


