from book import Book
from library import Library

def main():
    library = Library()
    book1 = Book("The Almanack of naval ravikanth", "eric", "9780743273565")
    book2 = Book("Atomic Habits", "James clear", "9780061120084")
    library.add_book(book1)
    library.add_book(book2)

    print("Books in library after initialization:")
    library.display_books()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            search_query = input("Enter title, author, or ISBN to search: ")
            library.search_books(search_query)

def print_menu():
    print("1. Display available books")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")

def main():
    library = Library()
    

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            search_query = input("Enter title, author, or ISBN to search: ")
            library.search_books(search_query)
        elif choice == "3":
            title = input("Enter the title of the book you want to borrow: ")
            library.borrow_book(title)
        elif choice == "4":
            title = input("Enter the title of the book you want to return: ")
            library.return_book(title)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
