# finally Block in Exception Handling :

# Example - 1 :
try:
    print('File opening code')
except FileNotFoundError as e:
    print(e)
finally:
    print('File closing code')



# Example - 2 (Exception raised and it handled) :
try:
    print(10+'surendra')
except TypeError as e:
    print(e)
finally:
    print('Finally block executed')


# Example - 3 (Exception raised and it does not handled) :
try:
    print(10+'surendra')
except FileNotFoundError as e:
    print(e)
finally:
    print('Finally block executed')


# Example - 4 :
try:
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print('File1 opening code')
    print('File2 opening code')
    print(8)
    print(9)
    print(10)
    print('File1 closing code')
    print('File2 closing code')
except FileNotFoundError as e:
    print(e)
finally:
    print('Finally block executed')


# Example - 5 :
try:
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print('File1 opening code')
    print('File2 opening code')
    print(8)
    print(9/0)
    print(10)
    print('File1 closing code')
    print('File2 closing code')
except FileNotFoundError as e:
    print(e)
finally:
    print('Finally block executed')


# Example - 6 :
try:
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print('File1 opening code')
    print('File2 opening code')
    print(8)
    print(9/0)
    print(10)
except FileNotFoundError as e:
    print(e)
finally:
    print('File1 closing code')
    print('File2 closing code')


# Some Sitution where finally block wont execute :
    
# 1) If we will forcefully stop the PVM :

import os
try:
    print(1)
    print(2)
    os._exit(0) #this code will shortdonw PVM
    print(3)
    print(4)
    print(5)
except Exception as e:
    print(e)
finally:
    print('Finally block executed')


# 2) Inside function if we will write finally block after return statement :
# Example - 1 :
def fun():
    try:
        print(1)
        print(2)
        print(3)
    except Exception as e:
        print(e)
    finally:
        print('Finally block executed')

fun()


# Example - 2 :
def fun():
    try:
        print(1)
        print(2/0)
        print(3)
    except Exception as e:
        print(e)
    finally:
        print('Finally block executed')

fun()


# Example - 3 :
def fun():
    try:
        print(1)
        return 'surendra'
        print(3)
    except Exception as e:
        print(e)
    finally:
        print('Finally block executed')

print(fun())


