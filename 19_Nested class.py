# Nested class / Inner class :
# a)
class Outer :
    def __init__(self) :
        print('Outer class constructor')
    
    class Inner :
        def __init__(self) :
            print('Inner class constructor')

o = Outer()   #Outer class object creation
i = o.Inner()  #Inner class object creation

i1 = Outer.Inner()   #Another way to create inner class object

i2 = Outer().Inner()   #Both outer and innner class object will create at the same time



# b) Inner class object creation inside Outer class :
class Outer :
    def __init__(self) :
        print('Outer class constructor')
    
    class Inner :
        def __init__(self) :
            print('Inner class constructor')

    i = Inner()

o = Outer()



# c) One outer class can contain multiple inner class :
class Outer :
    def __init__(self) :
        print('Outer class constructor')
    
    class Inner :
        def __init__(self) :
            print('Inner class constructor')

    class Inner1 :
        def __init__(self) :
            print('Inner class 1 constructor')


o = Outer()
i = o.Inner()
i1 = o.Inner1()



# d) Inner inner class :
class Outer :
    def __init__(self) :
        print('Outer class constructor')
    
    class Inner :
        def __init__(self) :
            print('Inner class constructor')

        class InnerInner :
            def __init__(self) :
                print('InnerInner class constructor')

o = Outer()
i = o.Inner()
i1 = i.InnerInner()

i2 = Outer.Inner.InnerInner()  #Another way to create nested nested class object 