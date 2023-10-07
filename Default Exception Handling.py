# Default Exception Handling || Exception Hierarchy :

# a)
#f = open('myfile.txt')


# b)
try :
    f = open('myfile.txt')

except FileNotFoundError :
    print('file does not exist')

print('Thank you')


print('-'*20)


# c)
try :
    f = open('myfile.txt')

except ZeroDivisionError :
    pass

print('Thank you')


# Note : All exception is the child of base exception.


# d)
l = [23, 33, 43, 53]
l[4] = 999
print(l)



# e)
l = [10, 20, 23, 33, 23, 11, 22, 44, 23]
print(l.index(789))



# f)
l = [10, 20, 30]
x = 999
l.extend(x)
print(l)



# g)
l = [23, 33, 43, 23, 53, 64, 23]
print(l)
del 1
print(l)



# h)
l = [23, 33, 43, 53, 64, 23]

for i in l :
    l.pop(i)

print(l)
