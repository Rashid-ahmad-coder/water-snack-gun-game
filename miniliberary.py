class liberay:
    def __init__(self, list_of_books, liberary_name):
        self.list_of_books=list_of_books
        self.liberary_name=liberary_name
        self.dict1={}

    def display_book(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}){books}")

    def lend_book(self,book, user):
        if book not in self.dict1.keys():
            self.dict1.update({book:user})
            print("lender book database has been updated, you can take the book now")
        else:
            print(f"Book is already lend by {self.dict1[book]}")

    def add_book(self,book):
            self.list_of_books.append(book)
            print("Your book is added successfylly")

    def return_book(self,book):
            self.list_of_books.pop(book)
            print(f"your book is returned successfully")


if __name__=='__main__':

    rashidlibrary = liberay(["python", "php", "c++", "c#", "java"], "rashidlibrary")
    print(f"Welcome to the {rashidlibrary.liberary_name}")
    print('Type d for display and l for lend, a for add and r for return books below:')
    while True:
        user_input=input("What do you want? display, lend, add or return of book:")
        if user_input=="d":
            rashidlibrary.display_book()

        elif user_input=="l":
            book=input("Enter the book you want to lend:")
            user=input("Enter your name:")
            rashidlibrary.lend_book(book,user)

        elif user_input=="a":
            book=input("Enter the book name:")
            rashidlibrary.add_book(book)

        elif user_input=="r":
            book=input("Enter the book you want to return:")
            rashidlibrary.return_book(book)

        else:
            print("Please check your input")

        user_input1=input("Press q to quit and c to continue")
        while(user_input1=="q" and user_input1=="c"):
            if user_input1=="q":
                exit()
            elif user_input1=="c":
                continue