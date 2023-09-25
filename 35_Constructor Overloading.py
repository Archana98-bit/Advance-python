# Constructor Overloading :
# Generally it is not supported :
# a)
class Test :
    def __init__(self, a) :
        print(a)
        
    def __init__(self, a, b) :
        print(a, b)

    def __init__(self, a, b, c) :
        print(a, b, c)

# t = Test(100)  #TypeError: Test.__init__() missing 2 required positional arguments: 'b' and 'c'

print('-'*20)



# b) Constructor overloading using multipledispatch method :

from multipledispatch import dispatch

class Test :
    
    @dispatch(int)
    def __init__(self, a) :
        print(a)
    
    @dispatch(int, int)
    def __init__(self, a, b) :
        print(a, b)

    @dispatch(int, int, int)
    def __init__(self, a, b, c) :
        print(a, b, c)

    @dispatch(int, int, float)
    def __init__(self, a, b, c) :
        print(a, b, c)

t = Test(10)
t1 = Test(10, 15)
t2 = Test(10, 28, 50)
t3 = Test(100, 34, 80.5)


