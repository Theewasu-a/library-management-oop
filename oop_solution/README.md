### Project Overview
    - This project is about managing books in a library, which helps you handle various complex actions related to books.

### Project Structure
    library-management-oop/
    │
    ├── README.md                     # This file
    │
    ├── procedural_version/
    ├── library_procedural.py         # Original procedural code
    ├── test_procedural.py            # Comprehensive test suite
    │   
    ├── oop_solution/
    │   ├── library_oop.py            # Student's OOP implementation (to create)
    │   └── test_oop.py               # Tests for OOP version (to create)

### Design Overview
    ├──Book Class
        - Attributes: id, title, author, total copies, available copies
        - Methods: Methods to manage book state

    ├── Member Class
        - Attributes: id, name, email, borrowed books list
        - Methods: Methods to manage borrowing

    ├── Library Class
        - Attributes: collections of books and members
        - Methods: add books, add members, borrow, return, and display operations

### Testing
    Basic Operations
        - Adding books and members
        - Borrowing and returning books
        - Displaying information

    Edge Cases
        - Borrowing unavailable books
        - Exceeding borrowing limit
        - Returning books not borrowed
        - Non-existent books/members

### How to run your test code
    Prepare the files library_oop.py and test_oop.py, run test_oop.py, and then compare its output with that of the provided procedural_version code.