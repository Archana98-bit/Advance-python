# File Handling :

# Example - 1 :
# Program to open and close a text file. 
f = open('About_jagannath.txt')
# print(type(f))
print(f) 
f.close()


# Example - 2 : (Different Modes) :

# 'W' - Mode :
f = open('About_hanuman.txt', mode='w')
f.close()


# Example - 3 :
# Program to open a file in 'w' mode and write some data on that file. 
f = open('About_sriram.txt', mode='w')
f.write('Jay sri ram\n')
f.write('Jay hanuman\n')
f.write('Ram mandir\n')
f.close()


# Example - 4 :
f = open('about_me.txt','w')
name = input('Enter your name: ')
mark = input('Enter your mark: ')
game = input('Enter your fav game: ')
f.write(name)
f.write(mark)
f.write(game)
f.close()


# Example - 5 :
# 'a' - Mode :

f = open('about_bbsr.txt', mode='a')
f.write('\nThis is a smart city\n')
f.write('Temple city\n')
f.close()


# Example - 6 :
# 'r+' - Mode :
f = open('About_jagannath.txt', mode='r+')
f.write('Welcome to puri dham\n')
f.close()

