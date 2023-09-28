# Abstract Class and Abstract Method :

# Abstract Class :
# a)
from abc import ABC, abstractmethod

class Shape(ABC) :
    
    @abstractmethod
    def area(self) :
        pass

class Circle(Shape) :
    def area(self,r) :
        print(f'area of circle : {3.14*r*r}')

class Square(Shape) :
    def area(self,s) :
        print(f'area of square : {s*s}')


c = Circle()
c.area(6)

s = Square()
s.area(5)


print('-'*20)



# b)
class Vehicle(ABC) :

    @abstractmethod
    def no_of_seats(self) :
        pass

    @abstractmethod
    def no_of_wheels(self) :
        pass

class Car(Vehicle) :
    def no_of_seats(self):
        print('Number of seats of a Car : 5')

    def no_of_wheels(self):
        print('Number of wheels of a Car : 4')


class Bus(Vehicle) :
    def no_of_seats(self):
        print('Number of seats of a Bus : 30')

    def no_of_wheels(self):
        print('Number of wheels of a Bus : 4')


class Auto(Vehicle) :
    def no_of_seats(self):
        print('Number of seats of a Auto : 2')

    def no_of_wheels(self):
        print('Number of wheels of a Auto : 3')


a = Auto()
a.no_of_seats()
a.no_of_wheels()

b = Bus()
b.no_of_seats()
b.no_of_wheels()

c = Car()
c.no_of_seats()
c.no_of_wheels()


print('-'*20)


# c) Customize :
class Vehicle(ABC) :
    
    @abstractmethod
    def no_of_seats(self) :
        pass

    @abstractmethod
    def no_of_wheels(self) :
        pass

class Car(Vehicle) :
    def no_of_seats(self, seats):
        print(f'Number of seats of a Car : {seats}')

    def no_of_wheels(self, wheels):
        print(f'Number of wheels of a Car : {wheels}')


class Bus(Vehicle) :
    def no_of_seats(self, seats):
        print(f'Number of seats of a Bus : {seats}')

    def no_of_wheels(self, wheels):
        print(f'Number of wheels of a Bus : {wheels}')


class Auto(Vehicle) :
    def no_of_seats(self, seats):
        print(f'Number of seats of a Auto : {seats}')

    def no_of_wheels(self, wheels):
        print(f'Number of wheels of a Auto : {wheels}')


a = Auto()
a.no_of_seats(2)
a.no_of_wheels(3)

b = Bus()
b.no_of_seats(20)
b.no_of_wheels(6)

c = Car()
c.no_of_seats(4)
c.no_of_wheels(4)


print('-'*20)


# d) abstract class contain abstract method as well as concrete method :

class Car(ABC) :

    @abstractmethod
    def no_of_seats(self) :
        pass
    
    def break_type(self) :
        print('Normal Break')

class Honda(Car) :
    def no_of_seats(self):
        print('Number of seats : 6')

class Audi(Car) :
    def no_of_seats(self):
        print('Number of seats : 4')

    def break_type(self):
        print('Special Break')

class SUV(Car) :
    def no_of_seats(self):
        print('Number of seats : 4')

    def break_type(self):
        print('Special with powerful Break')

class Coupe(Car) :
    def no_of_seats(self):
        print('Number of seats : 5')


h = Honda()
h.no_of_seats()
h.break_type()

a = Audi()
a.no_of_seats()
a.break_type()

s = SUV()
s.no_of_seats()
s.break_type()

c = Coupe()
c.no_of_seats()
c.break_type()


print('-'*20)


# e) Concrete class VS Abstract class :

# Example 1 :
class Test():
    def method1(self) :
        pass

t = Test()
t.method1()



# Example 2 :
from abc import ABC, abstractmethod

class Test(ABC) :

    @abstractmethod
    def ab1(self) :
        pass

# t = Test()   #TypeError: Can't instantiate abstract class Test with abstract method ab1



# Example 3 :

class Test(ABC) :
    def method1(self) :
        print('Hello!')

t = Test()



# Example 4 :

class Test(ABC) :
    def method1(self) :
        print('Hello!')

    @abstractmethod
    def ab1(self) :
        pass

class Child(Test) :
    def ab1(self) :
        print('Hii')

c = Child()
c.ab1()
c.method1()


print('-'*20)


# Example 5 :

class Test(ABC) :
    def method1(self) :
        print('Hello!')

    @abstractmethod
    def ab1(self) :
        pass

class Child(Test) :
    def ab1(self) :
        pass

c = Child()
c.ab1()
c.method1()


print('-'*20)


# Example 6 :
class Test(ABC) :
    def method1(self) :
        print('Hello!')

    @abstractmethod
    def ab1(self) :
        pass

class Child(Test) :
    pass

# c = Child()  #TypeError: Can't instantiate abstract class Child with abstract method ab1
c.ab1()
c.method1()


