# Hierarchical Inheritance :

class A :
    def method1(self) :
        self.x = 999
        print('-'*20)
        print('Parent class method1')

    def method2(self) :
        print('Parent class method2')

class B(A) :
    def method3(self) :
        print('Child class method3')
    
    def method4(self) :
        print('Child class method4')

class C(A) :
    def method5(self) :
        print('Child class method5')

    def method6(self) :
        print('Child class method6')

c = C()
c.method1()
c.method2()
c.method5()
c.method6()
print(c.x)

b = B()
b.method1()
b.method2()
b.method3()
b.method4()
print(b.x)

