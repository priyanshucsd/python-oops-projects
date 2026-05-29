users=[]
books=[]
def name():
    while True:
        name = input("Enter your name:")
        if name.isalpha():
            return name
        else:
            print("Invalid Name")

def age():
    while True:
        age = input("Enter your age:")
        if age.isnumeric():
            return age
        else:
            print("Invalid Age")
def roll():
    while True:
        roll = input("Enter your roll:")
        if roll.isnumeric():
            return roll
        else:
            print("Invalid Roll")
def role():
    while True:
        role = input("Enter your role (s for student / l for librarian)").lower()
        if role.isalpha():
            if role == "s" or role == "l":
                return role
            else:
                print("Invalid Role")
        else:
            print("Invalid selection")

def add_book():
    while True:
        book_name = input("Enter your book name:")
        if book_name.isalnum():
            return book_name
        else:
            print("Invalid Book name")



def book_quantity():
    while True:
        book_quantity = input("Enter your book quantity:")
        if book_quantity.isnumeric():
            book_quantity = int(book_quantity)
            return book_quantity
        else:
            print("Invalid Book quantity")


def delete_book():
    while True:
        book_name = input("Enter your book name:")
        if book_name.isalnum():

            for book in books:
                if book['book name'] == book_name:
                    books.remove(book)
                    print("book deleted")
                    break

            else:
                print("book not found")

        else:
            print("Invalid Book name")

        ch = input("do you want to delete a book?(y/n)").lower()
        if ch == "y":
            continue
        if ch == "n":
            break
        else:
            print("Invalid Choice")
            break

def show_books():
    if len(books)==0:
        print("No books found")
    else:
        for book in books:
            print(book)

def issue_book():

    while True:

        name = input("Enter your book name:")
        if name.isalnum():
            for book in books:
                if book['book name'] == name and book['book quantity']>0:
                    print("book issued")
                    book['book quantity']-=1
                    break
                elif book['book name'] == name and book['book quantity']==0:
                    print("book currently not available")
                    break
            else:
                print("book not found")
        else:
            print("Invalid book name")
        choice = input("Do you want to issue a new book?(y/n)").lower()
        if choice == "y":
            continue
        if choice == "n":
            break

def return_book():
    while True:
        name = input("Enter your book name:")
        if name.isalnum():
            for book in books:
                if book['book name'] == name and book['book quantity']>=0:
                    print("book returned")
                    book['book quantity']+=1
                    break
            else:
                print("book not found")
        else:
            print("Invalid book name")

        choice = input("Do you want to return a new book?(y/n)").lower()
        if choice == "y":
            continue
        if choice == "n":
            break

class Book:
    def add_book(self):
        while True:
            book={
                'book name':add_book(),
                'book quantity':book_quantity()
            }
            books.append(book)

            ch = input("do you want to add a new book?(y/n)").lower()
            if ch == "y":
                continue
            if ch == "n":
                break
            else:
                print("Invalid Choice")
                break
    def delete_book(self):

        delete_book()
    def show_books(self):

        show_books()
    def issue_book(self):

        issue_book()
    def return_book(self):

        return_book()
    def exit(self):
        print("Thank you for using this program")
        exit()


class Library(Book):
    def __init__(self):
        while True:
            user_input=input("1.Register\n2.Login\n3.Display\n4.Exit\nEnter your choice: ")
            if user_input.isnumeric():
                if user_input=='1':
                    user={
                        'name':name(),
                        'age':age(),
                        'roll':roll(),
                        'role':role(),
                    }
                    users.append(user)
                if user_input=='2':
                    login_name = name()
                    login_roll = roll()

                    found=False
                    for user in users:
                        if user['name'] == login_name and user["roll"] == login_roll and user['role']=='s':
                            print("student found , you are logged in")
                            while True:
                                stu_input=input("1.Issue book\n2.Return book\n3.Show available books\n4.exit\nEnter your choice: ")
                                if stu_input == "1":
                                    self.issue_book()
                                if stu_input == "2":
                                    self.return_book()
                                if stu_input == "3":
                                    self.show_books()
                                if stu_input == "4":
                                    break

                            found=True
                            break

                        if user['name'] == login_name and user["roll"] == login_roll and user['role'] == 'l':
                            print("librarian found , you are logged in")
                            while True:
                                lib_input=input("1.Add book\n2.Delete book\n3.Show available books\n4.exit\nEnter your choice: ")
                                if lib_input == "1":
                                    self.add_book()
                                if lib_input == "2":
                                    self.delete_book()
                                if lib_input == "3":
                                    self.show_books()
                                if lib_input == "4":
                                    break
                            found=True
                            break

                    else:
                        print("user not found")

                if user_input=='3':
                    if len(users) == 0:
                        print("no users has registered")
                    for user in users:
                        print('name:',user['name'],
                              'age:',user['age'],
                              'roll:',user['roll'],
                              'role:',user['role'])

                if user_input=='4':
                    break

u1=Library()



