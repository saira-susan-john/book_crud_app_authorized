from services.user_service import UserService
from services.book_service import BookService
from models.book import Book

db_config = {
    "dbname": "book_crud",
    "user": "postgres",
    "password": "admin123",
    "host": "localhost",
    "port": 5432,
}

user_service = UserService(db_config)
book_service = BookService(db_config)

token = None  

def book_menu():
    while True:
        print("\n--- Book Management ---")
        print("1. Add Book")
        print("2. Get Book by ID")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. List All Books")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = int(input("Enter ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = int(input("Enter Year: "))
            book = Book(id=id, title=title, author=author, year=year)
            book_service.add_book(book)
            print("Book added successfully.")

        elif choice == "2":
            id = int(input("Enter Book ID: "))
            book = book_service.get_book_by_id(id)
            if book:
                print(book)
            else:
                print("Book not found.")

        elif choice == "3":
            id = int(input("Enter Book ID to update: "))
            title = input("Enter new Title: ")
            author = input("Enter new Author: ")
            year = int(input("Enter new Year: "))
            updated_book = Book(id=id, title=title, author=author, year=year)
            if book_service.update_book(updated_book):
                print("Book updated.")
            else:
                print("Book not found.")

        elif choice == "4":
            id = int(input("Enter Book ID to delete: "))
            if book_service.delete_book(id):
                print("Book deleted.")
            else:
                print("Book not found.")

        elif choice == "5":
            books = book_service.list_all_books()
            if books:
                for book in books:
                    print(book)
            else:
                print("No books available.")

        elif choice == "6":
            print("Logging out of Book Management...")
            break

        else:
            print("Invalid choice. Try again.")

def start_app():
    global token

    while True:
        print("\n=== Welcome to Book CRUD App ===")
        print("1. Register")
        print("2. Login")
        print("3. Access Book Management")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_service.register_user(username, password)

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            token = user_service.login_user(username, password)
            if token:
                print("Login successful!")
                print(f"Your token: {token}")
            else:
                print("Login failed. Invalid credentials.")

        elif choice == "3":
            if token:
                print("Access granted. Launching Book Management...")
                book_menu()
            else:
                print("Please login to access Book Management.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    start_app()
