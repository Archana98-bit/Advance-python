# Interface :
# a)
from abc import ABC, abstractmethod

class Vehicle(ABC) :
    @abstractmethod
    def no_of_seats(self) :
        pass

    @abstractmethod
    def no_of_wheels(self) :
        pass

# we can not create the object for interface
#v = Vehicle() #TypeError: Can't instantiate abstract class Vehicle with abstract methods no_of_seats, no_of_wheels

        

# b)
class Vehicle(ABC) :
    @abstractmethod
    def no_of_seats(self) :
        pass

    @abstractmethod
    def no_of_wheels(self) :
        pass

class Bike(Vehicle) :
    def no_of_seats(self) :
        print("Seats : 2")

    def no_of_wheels(self) :
        print("Wheels : 2")

class Auto(Vehicle) :
    def no_of_seats(self) :
        print("Seats : 4")

    def no_of_wheels(self) :
        print("Wheels : 3")


b = Bike()
b.no_of_seats()
b.no_of_wheels()


a = Auto()
a.no_of_seats()
a.no_of_wheels()


print('-'*20)


# c)
class Vehicle(ABC) :
    @abstractmethod
    def no_of_seats(self) :
        pass

    @abstractmethod
    def no_of_wheels(self) :
        pass

class Bike(Vehicle) :
    def no_of_seats(self) :
        print("Seats : 2")

    def no_of_wheels(self) :
        print("Wheels : 2")

    def method1(self) :
        print("Extra method named as method1")

class Auto(Vehicle) :
    def no_of_seats(self) :
        print("Seats : 4")

    def no_of_wheels(self) :
        print("Wheels : 3")

    def method2(self) :
        print("Extra method named as method2")


b = Bike()
b.no_of_seats()
b.no_of_wheels()
b.method1()

a = Auto()
a.no_of_seats()
a.no_of_wheels()
a.method2()
