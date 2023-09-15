# Hybrid Inheritance :
class A :
    def method1(self) :
        print('A class method1')

class B(A) :
    def method2(self) :
        print('B class method2')

class C(A) :
    def method3(self) :
        print('C class method3')

class D(B,C) :
    def method4(self) :
        print('D class method4')

d = D()
d.method1()
d.method2()
d.method3()
d.method4()


# b)
class Bank :
    def __init__(self, bname, baddress, ifsc) :
        self.bname = bname
        self.baddress = baddress
        self.ifsc = ifsc
    
    def printBankDetails(self) :
        print('Bank Name : {self.bname}')
        print('Bank Address : {self.baddress}')
        print('Bank IFSC Code : {self.ifsc}')

class Customer1(Bank) :
    def __init__(self, c1name, c1address, c1account) :
        self.c1name = c1name
        self.c1address = c1address
        self.c1account = c1account
        self.b = Bank('State Bank of India', 'BBSR','1234OSBI7890')

    def printCustomer1Details(self) :
        print('Customer1 Name : {self.c1name}')
        print('Customer1 Address : {self.c1address}')
        print('Customer1 Account : {self.c1account}')
        self.b.printBankDetails()

class Customer2(Bank) :
    def __init__(self, c2name, c2address, c2account) :
        self.c2name = c2name
        self.c2address = c2address
        self.c2account = c2account

    def printCustomer2Details(self) :
        print('Customer2 Name : {self.c2name}')
        print('Customer2 Address : {self.c2address}')
        print('Customer2 Account : {self.c2account}')

class Employee(Customer1, Customer2) :
    def __init__(self, ename, eid) :
        self.ename = ename
        self.eid = eid
        self.c1 = Customer1('Priyanka','Kendrapara', 1234567)
        self.c2 = Customer2('Zini', 'Balasore', 654321)

    def printEmpDetails(self) :
        print('Employee Name : {self.ename}')
        print('Employee ID : {self.eid}')
        self.c1.printCustomer1Details()
        self.c2.printCustomer2Details()

e = Employee('Rahul', 1024)
e.printCustomer1Details()
e.printCustomer2Details()



