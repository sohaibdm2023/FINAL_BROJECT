class Book:
    def __init__(self, book_id, title, author, level):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.level = level
        self.available = True


class Member:
    def __init__(self, member_id, name, email, level):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_members(self):
        print("ID\t\t | Name\t\t\t | Email\t\t | Level\t\t\t ")
        print("=" * 80)
        for member in self.members:
            print(f"{member.member_id}\t\t | {member.name}\t\t | {member.email}\t\t | {member.level}")

    def display_books(self):
        print("ID\t | Title\t | Author\t | Level\t | Availability")
        print("=" * 80)
        for book in self.books:
            availability = "Available" if book.available else "Not Available"
            print(f"{book.book_id}\t | {book.title}\t\t | {book.author}\t\t | {book.level}\t\t | {availability}")

    def find_memberId(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_bookId(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None


library = Library()

welcome = "Welcome to the Library System"
print(welcome.center(100, "-"))
choices = ''' 
1.Add Member  
2.Edit Member  
3.Show members  
4.Delete Member 
5.Add Book 
6.Show Books 
7.Borrow Book 
8.Return Book 
9.Exit 
'''

while True:
    print(choices)
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        name1 = input("*Enter member name : ")
        email1 = input("*Enter member email : ")
        while email1.find("@") == -1:
            email1 = input("Invalid input! Please enter the Email again : ")
        level1 = input("*Enter the member level (A/B/C): ")
        while not (
                level1.lower() == "a" or level1.upper() == "A" or level1.lower() == "b" or level1.upper() == "B" or level1.lower() == "c" or level1.upper() == "C"):
            level1 = input(f"Invalid input! Please enter the Member Level again (A/B/C): ")
        print("# Member added successfully.")
        member_id = len(library.members) + 1
        new_member = Member(member_id, name1, email1, level1)
        library.add_member(new_member)

    elif choice == 2:
        member_id = int(input("*Enter Member ID : "))
        member = library.find_memberId(member_id)
        if member:
            name2 = input("*Enter member new name : ")
            email2 = input("*Enter member new email : ")
            level2 = input("*Enter the member new level (A/B/C) : ")
            while not (
                    level2.lower() == "a" or level2.upper() == "A" or level2.lower() == "b" or level2.upper() == "B" or level2.lower() == "c" or level2.upper() == "C"):
                level2 = input(f"Invalid input! Please enter the Member Level again (A/B/C): ")
            print("# Member details Updated successfully.")
            member.name = name2
            member.email = email2
            member.level = level2
        else:
            print("MemberID Not Found!!")

    elif choice == 3:
        library.display_members()

    elif choice == 4:
        member_id_to_delete = int(input("*Enter Member ID to delete : "))
        member_to_delete = None

        for member in library.members:
            if member.member_id == member_id_to_delete:
                member_to_delete = member
                break

        if member_to_delete:
            library.members.remove(member_to_delete)
            print("# Member deleted successfully.")
        else:
            print("MemberID Not Found!!")

    elif choice == 5:
        title = input("*Enter Book Title : ")
        author = input("*Enter Book Author : ")
        level1 = input("*Enter the book level (A/B/C): ")
        while not (
                level1.lower() == "a" or level1.upper() == "A" or level1.lower() == "b" or level1.upper() == "B" or level1.lower() == "c" or level1.upper() == "C"):
            level1 = input(f"Invalid input! Please enter the Book Level again (A/B/C): ")
        print("# Book added successfully.")
        book_id = len(library.books) + 1
        new_book = Book(book_id, title, author, level1)
        library.add_book(new_book)

    elif choice == 6:
        library.display_books()

    elif choice == 7:
        memberr_id = int(input("*Enter Member ID : "))
        book_id = int(input("*Enter Book ID : "))
        member = library.find_memberId(memberr_id)
        book = library.find_bookId(book_id)
        if member and book:
            if book.available and member.level.upper() == book.level.upper():
                book.available = False
                member.borrowed_books.append(book)
                print(f"#{member.name} has borrowed the book : {book.title} ")
            elif not book.available:
                print("#Book is not available for borrowing.")
            else:
                print("#Member level is not suitable for borrowing this  book  !!")
        else:
            print("Member or Book not Found !!")

    elif choice == 8:
        memberr_id = int(input("*Enter Member ID : "))
        book_id = int(input("*Enter Book ID : "))
        member = library.find_memberId(memberr_id)
        book = library.find_bookId(book_id)
        if member and book:
            for borrowed_book in member.borrowed_books:
                if borrowed_book == book:
                    book.available = True
                    member.borrowed_books.remove(book)
                    print(f"#{member.name} has returned the book : {book.title} ")
                else:
                    print("Sorry !! , Not found :(")
        else:
            print("Member or Book not Found !!")

    elif choice == 9:
        welcome = " Your Welcome Everyone :) "
        print(welcome.center(100,"*"))
        by = "**By : Wafaa Alastal and Suhaib Jalambo"
        print(by.center(100,"*"))
        eng = " Thank You Eng,Ghydaa :)  "
        print(eng.center(100,"*"))
        break
    else:
       print("Invalid choice. Please select a valid option.")
