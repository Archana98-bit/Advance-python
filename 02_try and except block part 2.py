# try except block flow of execution :

# Example - 1 :
try:
    print('surendra')
except ZeroDivisionError:
    print('u cant divide a number with zero')


# Example - 2 :
try:
    print(10/0)
except ZeroDivisionError:
    print('u cant divide a number with zero')



# Example - 3 :
try:
    print(10/0)
except ZeroDivisionError as z:
    print(z)


# Example - 4 :
print(10/0)


# Example - 5 :
try:
    print(10/0)
except ZeroDivisionError as ze:
    print(type(ze))
    print(ze)



# Example - 6 :
try:
    print(10/0)
except FileNotFoundError as e:
    print(e)
print('Thank You')



# Example - 7 :
try:
    print(10/0)
except FileNotFoundError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
print('Thank You')


# Example - 8 :
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
print('Thank You')


# Example - 9 :
try:
    print(1)
    print(2)
    print(10/0)
    print(3)
    print(4)
except ZeroDivisionError as e:
    print(e)
print('Thank You')



# Example - 10 :
try:
    print(10/0)
    print(10/0)
except ZeroDivisionError as e:
    print(e)
print('Thank You')



# Example - 11 :
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
    print(10+'surendra')
print('Thank You')



# Example - 12 :
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
    try:
        print(10+'surendra')
    except TypeError as e:
        print(e)
print('Thank You')



# Example - 13 :
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
    try:
        print(10+'surendra')
    except TypeError as e:
        print(e)
print('Thank You')



# Example - 14 :
try:
    print(10/0)
except ArithmeticError as e:
    print(e)
print('Thank You')



# Example - 15 :
try:
    print(10/0)
except Exception as e:
    print(e)
print('Thank You')



# Example - 16 :
try:
    print(10/0)
except BaseException as e:
    print(e)
print('Thank You')



# Example - 17 :
try:
    print(10+'surendra')
    try:
        print(10/0)
    except ZeroDivisionError as e:
        print(e)
except TypeError as e:
    print(e)

print('Thank You')



# Example - 18 :
try:
    print('10'+'surendra')
    try:
        print(10/0)
    except ZeroDivisionError as e:
        print(e)
except TypeError as e:
    print(e)

print('Thank You')



# Example - 19 :
try:
    print('10'+'surendra')
    try:
        print(10/0)
    except FileNotFoundError as e:
        print(e)
except TypeError as e:
    print(e)

print('Thank You')


# Example - 20 :
try:
    print('10'+'surendra')
    try:
        print(10/0)
    except FileNotFoundError as e:
        print(e)
except ZeroDivisionError as e:
    print(e)

print('Thank You')


# Example - 21 :
try:
    print('10'+'surendra')
    try:
        print(10/0)
    except FileNotFoundError as e:
        print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)
print('Thank You')



# TRY WITH MULTIPLE EXCEPT BLOCK :

# Example - 1 :
try:
    a=int(input('Enter the value for a : '))
    b=int(input('Enter the value for b : '))
    result=a/b
    print(result)
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)
print('Thank You')



# Example - 2 :

try:
    a=int(input('Enter the value for a : '))
    b=int(input('Enter the value for b : '))
    result=a/b
    print(result)
except ValueError as e:
    print(e)
    a=int(input('Enter the value for a : '))
    b=int(input('Enter the value for b : '))
    result=a/b
    print(result)
except ZeroDivisionError as e:
    print(e)
    print(a+b)
print('Thank You')


# Example - 3 :

try:
    a=int(input('Enter the value for a : '))
    b=int(input('Enter the value for b : '))
    result=a/b
    print(result)
except ValueError as e:
    print(e)
    try:
        a=int(input('Enter the value for a : '))
        b=int(input('Enter the value for b : '))
        result=a/b
        print(result)
    except Exception as e:
        print(e)
except ZeroDivisionError as e:
    print(e)
    print(a+b)
print('Thank You')



# SINGLE EXCEPT BLOCK CAN HANDEL MULTIPLE EXCEPTION :

# Example - 1 :
try:
    a=int(input('Enter the value for a : '))
    b=int(input('Enter the value for b : '))
    result=a/b
    print(result)
except (ZeroDivisionError,ValueError) as e:
    print(type(e))
    print(e)



# Default Except block :
    
# Example - 1 :
try:
    a=int(input('Enter the value for a : '))
    b=int(input('Enter the value for b : '))
    result=a/b
    print(result)
except:
    print('Someting goes wrong')



# Example - 2 :
try:
    a=int(input('Enter the value for a : '))
    b=int(input('Enter the value for b : '))
    result=a/b
    print(result)
except Exception as e:
    print(e)

