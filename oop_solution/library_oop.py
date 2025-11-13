class Book:
    def __init__(self, id, title, author, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.available_copies = available_copies

class Member:
    def __init__(self, id, name, email="N/A"):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []

    # ----------------- BOOK -----------------
    def add_book(self, id, title, author, total_copies):
        if any(book.id == id for book in self.books):
            print(f"Error: Book ID {id} already exists!")
            return
        book = Book(id, title, author, total_copies)
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    # ----------------- MEMBER -----------------
    def add_member(self, id, name, email="N/A"):
        if any(member.id == id for member in self.members):
            print(f"Error: Member ID {id} already exists!")
            return
        member = Member(id, name, email)
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully!")

    def find_member(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    # ----------------- BORROW,RETURN -----------------
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return False
        if not book:
            print("Error: Book not found!")
            return False
        if book.available_copies <= 0:
            print("Error: No copies available!")
            return False
        if len(member.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False

        # Borrow success
        book.available_copies -= 1
        member.borrowed_books.append(book)
        self.borrowed_books.append({
            "member_id": member.id,
            "member_name": member.name,
            "book_id": book.id,
            "book_title": book.title
        })
        print(f"{member.name} borrowed '{book.title}'")
        return True

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False
        if book not in member.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False

        # Return success
        book.available_copies += 1
        member.borrowed_books.remove(book)

        # remove record from borrowed_books
        self.borrowed_books = [
            tr for tr in self.borrowed_books
            if not (tr["member_id"] == member.id and tr["book_id"] == book.id)
        ]
        print(f"{member.name} returned '{book.title}'")
        return True

    # ----------------- DISPLAY -----------------
    def display_available_books(self):
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")
            else:
                continue

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        print(f"\n=== Books borrowed by {member.name} ===")
        if member.borrowed_books:
            for book in member.borrowed_books:
                print(f"  - {book.title} by {book.author}")
        else:
            print("  No books currently borrowed")