class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(self.title, self.author, self.pages + other.pages)

    def __del__(self):
        print('Book deleted!')

book1 = Book("abc", "def", 10)
book2 = Book("xyz", "ghi", 20)
result = book1 + book2
print(result)