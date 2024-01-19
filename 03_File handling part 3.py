# Write a program to collect set of name from the user one by one and store inside a file until press no.

f=open('List_of_names.txt','a+')

while True:
    name=input('Enter a name : ')
    if name=='no':
        print('Stop')
        break
    else:
        f.write(name+'\n')
    
f.close()



# Read data from the file :

# 1. read() :

# Example - 1 :
f=open('List_of_names.txt','r')
data=f.read()
print(data)


# Example - 2 :
f=open('List_of_names.txt','r')
data=f.read(4)
print(data)


# Example - 3 :
f=open('List_of_names.txt','r')
data=f.read(10)
print(data)


# Example - 4 :
f=open('List_of_names.txt','r')
data=f.read(8)
print(data)


# Example - 5 :
f=open('List_of_names.txt','r')
data=f.read(9)
print(data)



# 2. readline() : It will only give you the first line of the file.

f=open('List_of_names.txt','r')
data=f.readline()
print(data)



# 3. readlines() : Give you a list where the first first elemnet of the list is first line of the file and 
# second element of the list is the second line of the file and so on.

f=open('List_of_names.txt','r')
data=f.readlines()
print(data)

# OR, 
f=open('List_of_names.txt','r')
data=f.readlines()

for i in data:
    print(i,end='')



# Write a Program to find out the number of line of a file :

f=open('About_parbati.txt','r')
data=f.readlines()
print(len(data))



# Write a Program to find out the number of character in each line of a file :

f=open('About_parbati.txt','r')
data=f.readlines()
print(data)

count=1
for i in data:
    print(f'Line {count} = {len(i)-1} character')
    count=count+1



# Write the data into the file :
# 1. write() :

f=open('city.txt',mode='w')
f.write('BBSR\n')
f.write('CTC\n')
f.write('PURI\n')
f.write('BAM\n')
f.write('SAM\n')
f.close()


# 2. writelines() :
# Example - 1 :

f=open('friends.txt',mode='w')

l=['Surendra\n', 'Priyanka\n', 'Rahul\n','Zini\n', 'Jack\n', 'Scoot\n', 'Dev\n','Anjali\n', 'Smruti\n', 'Stalina\n'] 

f.writelines(l)

f.close()



# 2. writelines() :
# Example - 2 :

f=open('friends.txt',mode='w')

l=('Surendra\n', 'Priyanka\n', 'Rahul\n','Zini\n', 'Jack\n', 'Scoot\n', 'Dev\n','Anjali\n', 'Smruti\n', 'Salina\n')

f.writelines(l)

f.close()



