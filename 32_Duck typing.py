# Duck Typing :

# Examples :
# a)

a = 100
print(a)
print(type(a))

print('-'*20)

# b)

x = 34.98
print(x)
print(type(x))


print('-'*20)

# object ( methods )

class A :
    def method1(self) :
        print('A class method1')

class B :
    def method1(self) :
        print('B class method1')

class C :
    def method1(self) :
        print('C class method1')

def display(x) :
    x.method1()

a = A()
display(a)

b = B()
display(b)

c = C()
display(c)

