# Add and Display Books using OOP :
class Book :
    def __init__(self) :
        self.name = ''
        self.author = ''
        self.price = 0.0
        self.isbn = ''
    
    def inputBookDetails(self) :
        self.name = input('Enter Book Name :')
        self.author = input('Enter Author Name :')
        self.price = float(input('Enter Book Price :'))
        self.isbn = input('Enter Book ISBN Number :')
        print(f'{self.name} Book added successfully..')
        print('-'*20)


    def bookDisplay(self) :
        print(f'Book Name : {self.name}')
        print(f'Book Author : {self.author}')
        print(f'Book Price : {self.price}')
        print(f'Book ISBN : {self.isbn}')
        print('-'*20)

book_list = []

while True :
    choice= int(input('Enter your choice \n1.Add Book \n2.Display Book \n3.Stop\n'))

    if choice==1 :
        b = Book()
        b.inputBookDetails()
        book_list.append(b)

    elif choice==2 :
        if len(book_list) == 0 :
            print('Book is not available')
        for i in book_list :
            i.bookDisplay()
    
    elif choice==3 :
        print('Thnx for using application..')
        break
    else :
        print('Enter a valid option')


b = Book()
b.inputBookDetails()
b.bookDisplay()

print(book_list)
