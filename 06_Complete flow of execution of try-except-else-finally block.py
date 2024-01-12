# Complete flow of execution of try - except - else - finally block :
# Example - 1 :
try:
    print('1')
    print('2')
    print('3')
    print('4')
    print('5')
except Exception as e:
    print(e)
finally:
    print('end')


# Example - 2 :
try:
    print('1')
    print('2')
    print(23+'surendra')
    print('4')
    print('5')
except Exception as e:
    print(e)
finally:
    print('end')


# Example - 3 :
try:
    print('1')
    print('2')
    print(23+'surendra')
    print('4')
    print('5')
except FileNotFoundError as f:
    print(f)
finally:
    print('end')


# Example - 4 :
try:
    print('1')
    print('2')
    print(23+'surendra')
    print('4')
    print('5')
except:
    print('something wrong')
finally:
    print('end')


# Example - 5 :
try:
    print('1')
    print('2')
    print(23+'surendra')
    print('4')
    print('5')
except:
    print(e)
finally:
    print('end')


# Example - 6 :
try:
    print('1')
    print('2')
    print(23+'surendra')
    print('4')
    print('5')
except:
    try:
        print(e)
    except Exception as e:
        print(e)
finally:
    print('end')


# Example - 7 :
try:
    print(23+'surendra')
except:
    try:
        print(e)
    except TypeError as e:
        print(e)
finally:
    print('end')


# Example - 8 :
try:
    print(23+'surendra')
except:
    try:
        print(e)
    except TypeError as e:
        print(e)
    except NameError as n:
        print(n)
finally:
    print('end')


# Example - 9 :
try:
    print(23+'surendra')
except:
    try:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
    except NameError as n:
        print('Name error occur')
finally:
    print('end')


# Example - 10 :
try:
    print(23+'surendra')
except:
    try:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print('inner finally')
finally:
    print('end')


# Example - 11 :
try:
    print('1')
except Exception as e:
    print(e)
    print(23+'surendra')
    print('2')
finally:
    print('end')


# Example - 12 :
try:
    print(10/0)
except Exception as e:
    print(e)
    print(23+'surendra')
    print('2')
finally:
    print('end')


# Example - 13 :
try:
    print(10/0)
except Exception as e:
    print(e)
    print(23+'surendra')
    print('2')
else:
    print('i m else block')
finally:
    print('end')


# Example - 14 :
try:
    print('1')
except Exception as e:
    print(e)
    print(23+'surendra')
    print('2')
else:
    print('i m else block')
finally:
    print('end')


# Example - 15 :
try:
    print(10/0)
except Exception as e:
    print(e)
    try:
        print(23+'surendra')
    except Exception as e:
        print(e)
    print('2')
else:
    print('i m else block')
finally:
    print('end')


# Example - 16 :
try:
    print(10/10)
except Exception as e:
    print(e)
    try:
        print(23+'surendra')
    except Exception as e:
        print(e)
    print('2')
else:
    print('i m else block')
finally:
    print('end')


# Example - 17 :
import os
try:
    print(10/10)
except Exception as e:
    print(e)
    try:
        print(23+'surendra')
    except Exception as e:
        print(e)
        os._exit(0)
    print('2')
else:
    print('i m else block')
finally:
    print('end')


# Example - 18 :
import os
try:
    print(10/0)
except Exception as e:
    print(e)
    try:
        print(23+'surendra')
    except Exception as e:
        print(e)
        os._exit(0)
    print('2')
else:
    print('i m else block')
finally:
    print('end')


# Example - 19 :
try:
    print('1')
    print('2')
    print(10/0)
    print('3')
    try:
        print('4')
        print('5')
    except Exception as e:
        print(e)
except Exception as e:
    print(e)


# Example - 20 :
try:
    print('1')
    print('2')
    print(10/0)
    print('3')
    try:
        print('4')
        print('5')
    except Exception as e:
        print('test hi : ',e)
except Exception as e:
    print('test hello : ',e)


# Example - 21 :
try:
    print('1')
    print('2')
    print(10/5)
    print('3')
    try:
        print('4')
        print('5')
    except Exception as e:
        print('test hi : ',e)
except Exception as e:
    print('test hello : ',e)


# Example - 22 :
try:
    print('1')
    print('2')
    print(10/5)
    print('3')
    try:
        print('4')
        print('5')
    except Exception as e:
        print('test hi : ',e)
    finally:
        print('inner finally')
except Exception as e:
    print('test hello : ',e)
finally:
    print('outer finally')


# Example - 23 :
try:
    print(23+'surendra')
    try:
        print(23+'surendra')
    except Exception as e:
        print('test hi : ',e)
    finally:
        print('inner finally')
except Exception as e:
    print('test hello : ',e)
finally:
    print('outer finally')


# Example - 24 :
try:
    print('23'+'surendra')
    try:
        print(23+'surendra')
    except Exception as e:
        print('test hi : ',e)
    finally:
        print(10/0)
except Exception as e:
    print('test hello ',e)


# Example - 25 :
try:
    print('23'+'surendra')
    try:
        print(23+'surendra')
    except Exception as e:
        print('test hi : ',e)
    finally:
        print(10/0)
except FileNotFoundError as e:
    print('test hello ',e)


# Example - 26 :
try:
    print('23'+'surendra')
    try:
        print(23+'surendra')
    except Exception as e:
        print('test hi : ',e)
    finally:
        print(10/0)
except FileNotFoundError as e:
    print('test hello ',e)
except Exception as e:
    print(e) 


# Example - 27 :
try:
    print('23'+'surendra')
    try:
        print(23+'surendra')
    except Exception as e:
        print('test hi : ',e)
    finally:
        print('surendra')
        print(10/0)
        print('priyanka')
except FileNotFoundError as e:
    print('test hello ',e)
except Exception as e:
    print(e) 


# Example - 28 :
try:
    print('23'+'surendra')
    try:
        print(23+'surendra')
    except Exception as e:
        print('test hi : ',e)
    finally:
        print('surendra')
        print(10/2)
        print('priyanka')
except FileNotFoundError as e:
    print('test hello ',e)
except Exception as e:
    print(e) 


# Example - 29 :
def fun():
    if(1>1):
        return True
    else:
        return False
    return 100
    
    try:
        print(1)
    except Exception as e:
        print(e)
    finally:
        return 999
    
print(fun()) 


# Example - 30 :
def fun():
    try:
        return 100
    except:
        return 200
    finally:
        return 300
    
print(fun()) 


# Example - 31 :
def fun():
    
    return 50
    
    try:
        return 100
    except:
        return 200
    finally:
        return 300
    
print(fun()) 


# Example - 32 :
try:
    print('1')
finally:
    print('end')

