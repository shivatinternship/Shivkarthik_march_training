def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)

def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed")

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned")

def register_member(members, member_id):
    members.add(member_id)

def show_available(catalog, borrowed_books):
    print("\nAvailable Books")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            print(book_id, details)

def main():
    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 1, "Python Basics", "John Smith", 2020)
    add_book(catalog, 2, "Data Structures", "Alice Brown", 2019)
    add_book(catalog, 3, "Machine Learning", "David Lee", 2022)
    add_book(catalog, 4, "AI Fundamentals", "Sarah Wilson", 2021)

    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)
    register_member(members, 101)

    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    return_book(borrowed_books, 1)
    show_available(catalog, borrowed_books)
    print("\nMembers:", members)
    print("Borrowed Books:", borrowed_books)

main()