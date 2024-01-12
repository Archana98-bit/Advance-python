# Assertions in Exception Handling :
# Example - 1 :
a=100
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
assert a==100    # is this cond true then execute next code,
                 # if it is false raise exception and stop the flow of execution 
print(7)
print(8)
print(9)
print(10)


# Example - 2 :
a=100
print(1)
print(2)
print(3)
a=23
print(4)
print(5)
print(6)
assert a==100 
print(7)
print(8)
print(9)
print(10)


# Example - 3 :
a=100
print(1)
print(2)
print(3)
a=23
print(4)
print(5)
print(6)
assert a==100,'a is not 100 it modified' 
print(7)
print(8)
print(9)
print(10)


# Example - 4 :
l=['surendra','priyanka','rahul','zini','jack','scoot']

assert input('enter your name') in l
print('remaining code')


# Example - 5 :
l=['surendra','priyanka','rahul','zini','jack','scoot']

assert input('enter your name') in l,'this name is not present'
print('remaining code')


# Example - 6 :
l=['surendra','priyanka','rahul','zini','jack','scoot']

try:
    assert input('enter your name') in l,'this name is not present'
except AssertionError as e:
    print(e)
print('remaining code')


# Example - 7 :

l=['surendra','priyanka','rahul','zini','jack','scoot']

try:
    assert input('enter your name') in l,'this name is not present'
except AssertionError as e:
    print(e)
print('remaining code')


# Example - 8 :
l=['surendra','priyanka','rahul','zini','jack','scoot']

try:
    assert input('enter your name') in l
except AssertionError as e:
    print(e)
print('remaining code')

