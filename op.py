import getpass

Books = {}  
borrowed_books = []
class addBook:
    def adbook(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        ISBN = int(input("Enter book ISBN: "))
        genre = input("Enter book genre: ")
        if title in Books:
            print("Book already exist")
            return
        Books[title] = {
            "author": author,
            "ISBN": ISBN,
            "genre": genre,
            "is_borrowed": False
        }
        print("Book added")
        


class removeBook(addBook):
    def remove(self):
        book_name = input("Enter book you want to remove ")
        if book_name in Books:
            del Books[book_name]
            print("Book is removed")
        else:
            print("Book is not found")


class BorrowBook:
    def borrowBook(self):
        book_name = input("Enter book title name: ")
        if book_name in Books:
            if Books[book_name]["is_borrowed"]:
                print("It is borrowed ")
            else:
                Books[book_name]["is_borrowed"] = True
                borrowed_books.append(book_name)
                print("Borrowed.")
        else:
            print("not found")


class returnBook:
    def returBook(self):
        title = input("Enter book title  name you want to return: ")
        if title  in borrowed_books:
            borrowed_books.remove(title)
            Books[title]["is_borrowed"] = False
            print("Book has been returned ")
        else:
            print("You have not borrowed book")


class Login:
    def signin(self):
        self.user = input("Please enter username: ")     
        self.password = getpass.getpass(prompt='Password: ')
        print("Login successful")


class Display:
    def displaybook(self):
        if not Books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for title in Books:
                print(title)



class searchBooks:
    def LinearSearch(self, Books):
        book_name = input("Enter the book name to search: ")

        index = 0
        for title in Books:
            if title == book_name:
                print(f" book  is available at index", index )
                return
            index += 1

        print(" is not found.")
    def searchbyISBN(self):
      isbn = input("search book by ISBN")
    for title in Books: 
         if Books[title]["ISBN"] == isbn: 
             print()

    
    
            
if __name__ == "__main__":
    while True: 
        print("===== Welcome To Library Management System =====")
        print("0. Please login")
        print("1. Add book")
        print("2. Remove  book")
        print("3. Borrow  book")
        print("4. Return abook")
        print("5. Search  book")
        print("6. Display all the books")
        print("7. Exit")

        char = input("Enter your choice: ")
        
        if char == '0': 
            user_login = Login()
            user_login.signin()

        elif char == '1':
            adder = addBook()
            adder.adbook()

        elif char == '2':    
            remover = removeBook()
            remover.remove()

        elif char == '3':
            borrower = BorrowBook()
            borrower.borrowBook()

        elif char == '4':
            ret = returnBook()
            ret.returBook()

        elif char == '5':
            searcher = searchBooks()
            searcher.LinearSearch(Books)

        elif char == '6': 
            dis = Display()
            dis.displaybook()

        elif char == '7':
            print("Exiting system.")
            break

        else:
            print("Choose a correct option.")