# 'r+' - Mode :

f=open('About_sriram.txt',mode='r+')
f.write('Namo')
f.close()


# 'w+' - Mode :

f=open('About_sriram.txt',mode='w+')
f.write('Namo')
f.close()


# 'w+' - Mode :

f=open('About_parbati.txt',mode='w+')
f.write('Namo parbati')
f.close()



# 'a+' - Mode :

f=open('About_parbati.txt',mode='a+')
f.write('\nOmm nama sivaya')
f.close()


# 'a+' - Mode :

f=open('About_parbati1.txt',mode='a+')
f.write('\nOmm nama sivaya')
f.close()



# 'x' - Mode : 

f=open('About_parbati.txt',mode='x')
f.write('omm nama sibaya')
f.close()


# 'x' - Mode :

f=open('About_siba.txt',mode='x')
f.write('omm nama sibaya')
f.close()


# Program to read the data from the file and display output screen :

f=open('About_jagannath.txt',mode='r')
data=f.read()
print(data)
f.close()


# Properties and methods of file object :

f=open('About_jagannath.txt',mode='w+')

#print name of the file 
print(f'Name of the file is : {f.name}')

#print the file opening mode 
print(f'Mode of the file is : {f.mode}')

#print wheater the file readbale or not 
print(f'File is readable or not : {f.readable()}')

#print wheater the file writeable or not 
print(f'File is writeable or not : {f.writable()}')

#print wheater the file is close or not 
print(f'File is close or not : {f.closed}')

f.close()

#print wheater the file is close or not 
print(f'File is close or not : {f.closed}')



