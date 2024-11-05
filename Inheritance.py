# Library Management System
# Parent/Base/Superclass

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def displayinfo(self):
        return f"Book Title: {self.title}  Author: {self.author}"

#Child/Derived/Subclass
class LibraryBook(Book):
    def __init__(self,title,author,isbn,copies_available):
        super() .__init__(title,author)
        self.isbn=isbn
        self.copies_available=copies_available

    def borrow_book(self):
        if self.copies_available>0:
            self.copies_available-=1
            return f"{self.title} borrowed.copies left {self.copies_available}"
        else:
            return f"No of copies {self.title} available"

    def return_book(self):
        self.copies_available+=1
        return f"{self.title} returned. copiies left {self.copies_available}"

book1=LibraryBook(title="Gifted Hands", author="Ben Carson", isbn=676734, copies_available=15 )
print(book1.displayinfo())
print(book1.borrow_book())
print(book1.borrow_book())
print(book1.return_book())