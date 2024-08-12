from database import execute_query, fetch_one

def display_main_menu():
    """
    Displays the main menu options.
    """
    print("\nWelcome to the Library Management System!")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def display_book_menu():
    """
    Displays the book operations menu options.
    """
    print("\nBook Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def display_user_menu():
    """
    Displays the user operations menu options.
    """
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

def display_author_menu():
    """
    Displays the author operations menu options.
    """
    print("\nAuthor Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

def add_book():
    """
    Adds a new book to the database.
    """
    title = input("Enter book title: ")
    author_id = int(input("Enter author ID: "))
    isbn = input("Enter ISBN: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    query = """
    INSERT INTO books (title, author_id, isbn, publication_date)
    VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (title, author_id, isbn, publication_date))
    print("Book added successfully!")

def borrow_book():
    """
    Allows a user to borrow a book.
    """
    user_id = int(input("Enter user ID: "))
    book_id = int(input("Enter book ID: "))
    borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
    query = """
    INSERT INTO borrowed_books (user_id, book_id, borrow_date)
    VALUES (%s, %s, %s)
    """
    execute_query(query, (user_id, book_id, borrow_date))
    print("Book borrowed successfully!")

def return_book():
    """
    Allows a user to return a book.
    """
    borrowed_id = int(input("Enter borrowed book ID: "))
    return_date = input("Enter return date (YYYY-MM-DD): ")
    query = """
    UPDATE borrowed_books
    SET return_date = %s
    WHERE id = %s
    """
    execute_query(query, (return_date, borrowed_id))
    print("Book returned successfully!")

def search_book():
    """
    Searches for a book in the database by title or ISBN.
    """
    search_term = input("Enter book title or ISBN to search: ")
    query = """
    SELECT b.id, b.title, a.name, b.isbn, b.publication_date, b.availability
    FROM books b
    JOIN authors a ON b.author_id = a.id
    WHERE b.title LIKE %s OR b.isbn = %s
    """
    results = execute_query(query, (f"%{search_term}%", search_term))
    if results:
        for row in results:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}, Publication Date: {row[4]}, Available: {row[5]}")
    else:
        print("No books found.")

def display_all_books():
    """
    Displays all books in the database.
    """
    query = """
    SELECT b.id, b.title, a.name, b.isbn, b.publication_date, b.availability
    FROM books b
    JOIN authors a ON b.author_id = a.id
    """
    results = execute_query(query)
    if results:
        for row in results:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}, Publication Date: {row[4]}, Available: {row[5]}")
    else:
        print("No books found.")

def add_user():
    """
    Adds a new user to the database.
    """
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    query = """
    INSERT INTO users (name, library_id)
    VALUES (%s, %s)
    """
    execute_query(query, (name, library_id))
    print("User added successfully!")

def view_user_details():
    """
    Views details of a user by ID.
    """
    user_id = int(input("Enter user ID: "))
    query = """
    SELECT * FROM users WHERE id = %s
    """
    user = fetch_one(query, (user_id,))
    if user:
        print(f"ID: {user[0]}, Name: {user[1]}, Library ID: {user[2]}")
    else:
        print("User not found.")

def display_all_users():
    """
    Displays all users in the database.
    """
    query = """
    SELECT * FROM users
    """
    results = execute_query(query)
    if results:
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Library ID: {row[2]}")
    else:
        print("No users found.")

def add_author():
    """
    Adds a new author to the database.
    """
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    query = """
    INSERT INTO authors (name, biography)
    VALUES (%s, %s)
    """
    execute_query(query, (name, biography))
    print("Author added successfully!")

def view_author_details():
    """
    Views details of an author by ID.
    """
    author_id = int(input("Enter author ID: "))
    query = """
    SELECT * FROM authors WHERE id = %s
    """
    author = fetch_one(query, (author_id,))
    if author:
        print(f"ID: {author[0]}, Name: {author[1]}, Biography: {author[2]}")
    else:
        print("Author not found.")

def display_all_authors():
    """
    Displays all authors in the database.
    """
    query = """
    SELECT * FROM authors
    """
    results = execute_query(query)
    if results:
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Biography: {row[2]}")
    else:
        print("No authors found.")

def main():
    """
    Main function to display the menu and handle user input.
    """
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                display_book_menu()
                book_choice = input("Enter your choice: ")
                if book_choice == '1':
                    add_book()
                elif book_choice == '2':
                    borrow_book()
                elif book_choice == '3':
                    return_book()
                elif book_choice == '4':
                    search_book()
                elif book_choice == '5':
                    display_all_books()
                else:
                    break

        elif choice == '2':
            while True:
                display_user_menu()
                user_choice = input("Enter your choice: ")
                if user_choice == '1':
                    add_user()
                elif user_choice == '2':
                    view_user_details()
