#<=================Library Management System ================>
import getpass
Books = []
class Library:
    def __init__(self):
        self.title = input("Enter the book title: ")
        self.author = input("Enter the book author: ")
        self.ISBN = int(input("Enter the book ISBN: "))
        self.genre = input("Enter the book genre: ")

    def detailsBook(self):
        print(f"Book details: {self.title}, {self.author}, {self.ISBN}, {self.genre}") 
   


class removeBook(Library):
    def remove(self):
        print("Enter the book name you want to remove")
        book_name = input("Enter the book name: ")
        for book in Books:
            if book.title == book_name: 
             Books.remove(book)
             print("Book has sucessfully removed")
            else:
             print("book is not found")
class borrowBook(Library):
    def borrow(self):
        print("Enter the book name you want to borrow")
        book_name = input("Enter the book name: ")
        if book_name == self.title:
            print("Book has been borrowed successfully")
        else:
            print("Book not found in the library")
class returnBook(Library):
    def returBook(self):
        print("Enter the book name you want to return")
        book_name = input("Enter the book name: ")
        if book_name == self.title:
            print("Book has been returned successfully")
        else:
            print("Book not found in the library")
        
class Login:
    def signin(self):
        self.user = input("Please enter your username: ")
        self.password = getpass.getpass(prompt='Password: ')
        print("Login successful! ")
class Display: 
    def displaybook(self):
     for book in Books:
        return book 


if __name__ == "__main__":
    while True: 
        print("\nWelcome To Library Management System")
        print("0. Please login")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Return a book")
        print("4. Display all the books")
        print("5. Exit")

        ch = input("Enter your choice: ")
        if ch =='0': 
         user_login = Login()
         user_login.signin()

        elif ch == '1':
            new_book = Library()       
            new_book.detailsBook() 
            Books.append(new_book)
        elif ch == '2':    
            remove_book = removeBook()
            remove_book.remove()
        elif ch == '3':
            return_book = returnBook()
            return_book.returBook()
        elif ch == '5':
            print("Exiting system")
            break
        else:
            print("Choose correct option .")
