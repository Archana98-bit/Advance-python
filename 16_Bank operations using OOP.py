# MINI PROJECT :

# Bank Operations using OOP :
class Bank :
    bankname = "State bank of india"
    branch = "Sector21, Janpath tower, New delhi, India"
    #Account creation
    def __init__(self, username, pan, address) :
        self.username = username
        self.pan = pan
        self.address = address
        self.balance = 0.0   #set account balance to 0.0
        print(f'Hello {self.username} congratulations! your a/c created successfully')

    #deposite
    def deposit(self, amount) :
        self.balance = self.balance + amount
        print(f'{amount} deposited successfully')
    #withdraw
    def withdraw(self,amount) :
        if amount < self.balance :
            self.balance = self.balance - amount
            print(f'{amount} withdraw successfully')
        else :
            print('Insufficient balance...')
        
    #ministatement
    def ministatement(self) :
        print(f'Your account balance is {self.balance}')
        
 
print(f'Welcome to {Bank.bankname}, {Bank.branch}')
#collect user data for account creation
username = input('Enter your name :')
pan = input('Enter your PAN card number :')
address = input('Enter your address :')

b = Bank(username, pan, address)   #object creation based on user provided data

while True :
    print('\nPlease Select any Option :')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n4.Close')
    option = int(input(''))

    if option==1 :
        amount=float(input('Enter the amount to be deposited :'))
        b.deposit(amount)

    elif option==2 :
        amount =float(input('Enter the withdrawal amount :'))
        b.withdraw(amount)

    elif option==3 :
        b.ministatement()

    elif option==4 :
        print('Thanks for using State bank of india..')
        break
    else :
        print('Invalid option, please select a valid option')
