# Encapsulation :

# prevent accidental modification :

class College :
    def __init__(self) :
        self.balance = 500000

c = College()
print(c.balance)

c.balance = 100
print(c.balance)


print('-'*20)

# prevention accidental modification :

class College :
    def __init__(self) :
        self._balance = 500000   # for private variable   # data hiding

c = College()
# print(c.balance)   #AttributeError: 'College' object has no attribute 'balance'. Did you mean: '_balance'?



# encapsulation :

class College :
    def __init__(self) :
        self.__balance = 500000   # for private variable   # data hiding

    def getBalance(self) :
        return self.__balance


c = College()
print(c.getBalance())


print('-'*20)


# a)

class College :
    def __init__(self) :
        self.__balance = 500000   # for private variable   # data hiding

    def getBalance(self, password) :
        if password == 'archana98@' :   # for authorized person accessing
            return self.__balance
        
        else :
            return "Invalid user"

c = College()
# print(c.getBalance())   #TypeError: College.getBalance() missing 1 required positional argument: 'password'

print(c.getBalance('archu123@'))


print('-'*20)


# b)

class College :
    def __init__(self) :
        self.__balance = 500000   # for private variable   # data hiding

    def getBalance(self, password) :
        if password == 'archana98@' :   # for authorized person accessing
            return self.__balance
        
        else :
            return "Invalid user"

c = College()
print(c.getBalance('archana98@'))



print('-'*20)


# c)

class College :
    def __init__(self) :
        self.__balance = 500000   # for private variable   # data hiding

    def getBalance(self, password) :
        if password == 'archana98@' or password == 100245 :   # for authorized person accessing
            return self.__balance
        
        else :
            return "Invalid user"

c = College()
print(c.getBalance('archana98@'))
print(c.getBalance(100245))   # for another authorozed person
print(c.getBalance(100243)) 
