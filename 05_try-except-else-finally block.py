# try - except - else - finally block in Exception Handling :

# Example - 1 :
try:
    print(10/0)
except ZeroDivisionError as z:
    print(z)
else:
    print('i m else block')    # here else block is not executing  beacuse of there is an execption in try block


# Example - 2 :
try:
    print(10/2)
except ZeroDivisionError as z:
    print(z)
else:
    print('i m else block')    # here else block is executing beacuse of there is not execption in try block


# Example - 3 : (Normal functional way) :
def add(a,b):
    print(a+b)
    
add(10,20)


# In try - except - else way :
def add(a,b):
    try:
        result=a+b
    except TypeError as t:
        print(t)
    else:
        print('addition result is : ',result)
    
add(10,'surendra')


# Example - 4 :
def add(a,b):
    try:
        result=a+b
    except TypeError as t:
        print(t)
    else:
        print('addition result is : ',result)
    
add(10,20)
add('rahul',10)
add(500,150)


# Example - 5 : (try - except - else - finally way) :
def add(a,b):
    try:
        result=a+b
    except TypeError as t:
        print(t)
    else:
        print('addition result is : ',result)
    finally:
        print('clean-up code')
add(10,20)
add('rahul',10)
add(500,150)


# Example - 6 :
# Order is importanat ( we can't change the order ) :
def add(a,b):
    try:
        result=a+b
    except TypeError as t:
        print(t)
    finally:
        print('clean-up code')
    else :
        print('addition result is: ', result)
    
add(10,20)


# Example - 7 :
# order is importanat ( we can't change the order ) :
def add(a,b):
    try:
        result=a+b
    else:
        print('addition result is : ',result)
    except TypeError as t:
        print(t)
    finally:
        print('clean-up code')
    
add(10,20)

