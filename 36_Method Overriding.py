# Method Overriding :
# a) Normal Example :
class Parent :
    def method1(self) :
        print('I like old songs')

class Child(Parent) :
    pass

c = Child()
c.method1()


print('-'*20)

# b) Overriding Examples :
class Parent :
    def method1(self) :
        print('I like old songs')

class Child(Parent) :
    def method1(self) :
        print('I like new songs')

c = Child()
c.method1()


print('-'*20)

# c)

class Circle :
    def area(self, r) :
        print(3.14*r*r)

class Triangle(Circle) :
    def area(self, b, h) :
        print(0.5*b*h)

class Square(Circle) :
    def area(self, s) :
        print(s*s)

s = Square()
s.area(3.5)

t = Triangle()
t.area(2.2, 5.6)


print('-'*20)


# d)
class Parent :
    def scooty(self) :
        print('I like Activa Scooty')
    
    def mob(self) :
        print('I like oppo f15')

class Child(Parent) :
    def mob(self) :
        print('I like MI')

c = Child()
c.scooty()
c.mob()


print('-'*20)

# e)
class Parent :
    def scooty(self) :
        print('I like HERO Scooty')
    
    def mob(self) :
        print('I like 1+ mobile')

class Child(Parent) :
    def mob(self) :
        super().scooty()
        print('I like iphone')

c = Child()
c.mob()

