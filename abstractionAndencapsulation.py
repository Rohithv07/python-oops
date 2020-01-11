class Library:
    def __init__(self,listOFBooks):
        self.availableBooks=listOFBooks

    def displayAvailable(self):
        print("Available Books")
        for book in self.availableBooks:
            print(book)


    def lentBook(self,requestedBook):
        if requestedBook in self.availableBooks:
            print("you have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Not available")
    def addBook(self,returnedBook):
        self.availableBooks.append(returnedBook)
        print("Book returned")
        
class Customer:
    def requestBook(self):
        print("Enter the name of the book:")
        self.book=raw_input()
        return self.book
    def returnBook(self):
        print("Enter the name of the book returning:")
        self.book=raw_input()
        return self.book


library=Library(['pass','ppp','aaa'])
customer=Customer()
while True:
    print("Enter 1 to display the book")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")

    userChoice=int(input())
    if userChoice is 1:
        library.displayAvailable()
    elif userChoice is 2:
        requestedBook=customer.requestBook()
        library.lentBook(requestedBook)
    elif userChoice is 3:
        returnedBook=customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
         quit()