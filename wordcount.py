Books = {}
class addBook:
    def __init__ (self, title):
     self.title = title 

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
        return title
        
obj = addBook() 
last_title = obj.adbook()
print(Books[last_title])