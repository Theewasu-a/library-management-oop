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