from library_oop import Library

def test_library_system():
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - OOP TEST")
    print("=" * 60)

    library = Library()

    # TEST 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    library.add_book(4, "Design Patterns", "Gang of Four", 2)

    # TEST 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    library.add_member(101, "Alice Smith", "alice@gmail.com")
    library.add_member(102, "Bob Jones", "bob@gmail.com")
    library.add_member(103, "Carol White", "carol@gmail.com")

    # TEST 3: Display Available Books ---
    print("\n--- TEST 3: Display Available Books ---")
    library.display_available_books()

    # TEST 4: Successful Borrowing ---
    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(101, 1)  # Alice borrows Python
    library.borrow_book(101, 2)  # Alice borrows Clean Code
    library.borrow_book(102, 1)  # Bob borrows Python


    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    library.display_member_books(101)
    library.display_member_books(102)
    library.display_member_books(103)

    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_available_books()

    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    library.borrow_book(103, 3)  # Carol borrows Pragmatic Programmer
    library.display_available_books()

    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(102, 3)  # Bob tries unavailable


    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    library.borrow_book(101, 4) # Alice's 3rd book
    library.display_member_books(101)
    library.borrow_book(101, 3) # Alice tries to borrow 4th book (should fail)

    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    library.return_book(101, 1)
    library.return_book(102, 1)
    library.display_member_books(101)
    library.display_available_books()

    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(102, 2)

    # --- TEST 12: Return and Re-borrow ---
    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(103, 3)
    library.borrow_book(102, 3)
    library.display_member_books(102)

    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 1)
    library.borrow_book(101, 999)
    library.return_book(999, 1)
    library.display_member_books(999)

    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for t in library.borrowed_books:
        print(f"  {t['member_name']} has '{t['book_title']}'")

    print("\nAll Members and Their Books:")
    for m in library.members:
        print(f"\n{m.name} ({m.id}):")
        if m.borrowed_books:
            for b in m.borrowed_books:
                print(f"  - {b.title}")

        else:
            print("  (No books borrowed.)")

    library.display_available_books()

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_library_system()