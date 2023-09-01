# Instance Method :
# a)
class Calculation :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    
    def add(self) :
        result1 = self.x + self.y
        print(f'addition is {result1}')
    
    def sub(self) :
        result2 = self.x - self.y
        print(f'substraction is {result2}')
        
c1 = Calculation(100, 200)
c1.add()

c2 = Calculation(100, 80)
c2.sub()


# b) call instance method inside another instance method :
class Calculation :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    
    def add(self) :
        result = self.x + self.y
        print(f'addition is {result}')
        self.sub()
    
    def sub(self) :
        result = self.x - self.y
        print(f'substraction is {result}')

c1 = Calculation(300, 200)
c1.add()



# c) call instance method outside of the class as well as inside of class :
class Calculation :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    
    def add(self) :
        result = self.x + self.y
        print(f'addition is {result}')
        self.sub()
    
    def sub(self) :
        result = self.x - self.y
        print(f'substraction is {result}')

c1 = Calculation(30, 20)
c1.add()       
c1.sub() 






# d) by using instance method we can operate modify, delete etc.
class Test :
    def __init__(self, a, b) :
        self.a = a
        self.b = b
    
    def update(self, x, y) :
        self.a = x
        self.b = y

    def delete(self) :
        del self.a

t1 = Test(10, 20)
print(t1.__dict__)

t1.update(100, 300)
print(t1.__dict__)

t1.delete()
print(t1.__dict__)

