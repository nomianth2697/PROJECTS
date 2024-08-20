class library:
    def __init__(self):
        self.books = []
        self.noofbooks=0

    def add_book(self,book):
        self.books.append(book)
        self.noofbooks = len(self.books)

    def no_of_books(self) :
        print(f"{self.noofbooks}")

    def all_books_of_library(self):
        for b in self.books:
            print(b)
        
print("------------welcome to yours library------------------")

b = library()


while True:
    print()
    a = int(input("if you have to add any book in library press 1"
"\nif you have no of books in your library press 2"
"\nif you have to see all books of library press 3"
"\nfor exit enter 4\n"))
    print()
    if a==1:
        book = input("enter name of book\n")
        b.add_book(book)
    elif a==2:
        b. no_of_books()
    elif a==3:
       b.all_books_of_library()
    elif a==4:
        print("your exited from libreary managment system")
        break
    else:
        print("invalid input")
        
print("thanks for visiting have a nice day")














