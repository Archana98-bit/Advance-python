# Static Method :
# a) calling static method outside of the class :
class Calculation :
    @staticmethod
    def add(a, b) :
        print(f'Addition is {a+b}')

    @staticmethod
    def mul(a, b) :
        print(f'Multiplication is {a*b}')

Calculation.add(100, 200)  #calling static method using class name

c1 = Calculation()  #by using object referance
c1.add(10, 30)


# b) calling static method inside the class :
class Calculation :
    @staticmethod
    def add(a, b) :
        print(f'Addition is {a+b}')
        Calculation.sub(243, 39)  #calling static method inside the class using class name

    @staticmethod
    def sub(a, b) :
        print(f'Substraction is {a-b}')

Calculation.add(22, 33)

