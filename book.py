class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    def compare_title(self, other_title):
        return self.title.lower() == other_title.lower()