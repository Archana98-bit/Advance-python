# try and except block :

# ZeroDivisionError:
# Exception :

a=int(input('Enter the value a : '))
b=int(input('Enter the value b : '))
print(a/b)         #ZeroDivisionError: division by zero
print('thank you')

# Solution :

a=int(input('Enter the value a : '))
b=int(input('Enter the value b : '))
try:
    print(a/b) 
except ZeroDivisionError:
    print('hey you can not divide any number with zero ')
print('thank you')


# Example :
a=int(input('Enter the value a : '))
b=int(input('Enter the value b : '))
try:
    print(a/b) 
except IndexError:    #bymistake we have written IndexError instead of ZeroDivisionError
    print('hey u can not divide any number with zero ')
print('thank you')


# Solving by if else method :
# if else :

a=int(input('Enter the value a : '))
b=int(input('Enter the value b : '))

if b!=0:
    print(a/b)
else:
    print('hey u can not divide any number with zero ')
print('thank you')


# Example :
# If the user will provide the value of b is 0 then instraed of division, add both value a and b.  

a=int(input('Enter the value a : '))
b=int(input('Enter the value b : '))

try:
    print(a/b)
except ZeroDivisionError:
    print(a+b)  # handling or alternative code 
print('Thnak you')



# Example :
a=int(input('Enter the value a : '))
b=int(input('Enter the value b : '))

try:
    print(a/b)
except ZeroDivisionError:
    print(a/b)  # During handling of the above exception, another exception occurred.
print('Thnak you')



# NameError :
# Exception :

print(a)   # NameError: name 'a' is not defined.
print('Thank you')


# Solution :
try:
    print(a)
except NameError:
    print('first define a then access')
print('Thank You')



# TypeError :
# Exception :

x=int(input('enter x value : '))
y=input('enter y value : ')
print(x+y)      # TypeError: unsupported operand type(s) for +: 'int' and 'str'.
print('thank you')


# Solution :

x=int(input('enter x value : '))
y=input('enter y value : ')

try:
    print(x+y)
except TypeError:
    print('Both x and y value must be of same type')

print('thank you')



# ValueError :
# Exception :

x = int(input('enter x value : '))   # ValueError: invalid literal for int() with base 10: 'SURENDRA'.
print('thank you')


# Soliution :
try:
    x=int(input('enter x value : '))
except ValueError:
    print('Plz provide a numeric value')
print('thank you')



# IndexError : 
# Exception :

l=[10,20,30,40,50]
index=int(input('Enter the index : '))
print(l[index])   # IndexError: list index out of range.
print('thank you')


# Solution :

l=[10,20,30,40,50]
index=int(input('Enter the index : '))

try:
    print(l[index])
except IndexError:
    print(f'Hey provide the index in between 0 to {len(l)-1}')
print('thank you')



# KeyError :
# Exception :

d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}

print(d[99])   # KeyError: 99
print('thank you')


# Solution :

d={23:'surendra',24:'priyanka',25:'rahul',26:'zini'}
key=int(input('Enter the key : '))

try:
    print(d[key])
except KeyError:
    print(f'{key} Key is not avaiable, and the keys are {d.keys()}')
print('Thank You')


# FileNotFoundError :
# Exception :

f=open('xyz.txt')   # FileNotFoundError: No such file or directory: 'xyz.txt'.
print('thank you')


# Solution : 

try:
    f=open('xyz.txt')
except FileNotFoundError:
    print('please provide a valid file name ')
print('Thnak You')


# ModuleNotFoundError :
# Exception :

import numpy23   # ModuleNotFoundError: No module named 'numpy23'.
print('thank you')

# Solution :

try:
    import numpy23
except ModuleNotFoundError:
    print('Cross verify your module')
print('thank you')


# OverflowError :
# Exception :

import math 

print(math.factorial(65545456456456745647456478674658))   # OverflowError: factorial() argument should not exceed 9223372036854775807
print('thank you')


# Solution : 

import math 

try:
    print(math.factorial(65545456456456745647456478674658))
except OverflowError:
    print('overflow the argumenet value')
print('thank you')


# IndentationError :
# Exception :
if 10>100:
print('hello')   # IndentationError: expected an indented block after 'if' statement on line 222.
print('hi')
print('thank you')


#solution 

try:
    if 10>100:
    print('hello')    # IndentationError: expected an indented block after 'if' statement on line 2
    print('hi')       # IndentationError is a special Error. You can not handle it.
except IndentationError:
    print('IndentationError occur')
print('thank you')


