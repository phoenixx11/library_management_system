import pickle

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = {}
        self.load_library()

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {'Yes' if book.available else 'No'}")

    def search_books(self, query):
        found_books = []
        query_lower = query.lower()
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query == book.isbn:
                found_books.append(book)
        if found_books:
            print("Found books matching your query:")
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {'Yes' if book.available else 'No'}")
        else:
            print("No books found matching your query.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    borrower_name = input("Enter your name: ")
                    due_date = input("Enter due date (YYYY-MM-DD): ")
                    book.available = False
                    self.borrowers[book] = (borrower_name, due_date)
                    print(f"{title} has been lent to {borrower_name}.")
                else:
                    print(f"{title} is not available.")
                return
        print("Book not found.")
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"{title} has been returned.")
                else:
                    print(f"{title} is already available.")
                return
        print("Book not found.")
    def load_library(self):
        try:
            with open("library_data.pkl", "rb") as f:
                self.books, self.borrowers = pickle.load(f)
        except FileNotFoundError:
            print("No existing library data found.")
        except Exception as e:
            print("Error loading library data:", e)

    def save_library(self):
        try:
            with open("library_data.pkl", "wb") as f:
                pickle.dump((self.books, self.borrowers), f)
        except Exception as e:
            print("Error saving library data:", e)
