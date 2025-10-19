class Book:
    def __init__(self, title: str, author: str, genre: str, available: bool):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        print(self.title, self.author, self.genre, self.available)

    def borrow(self):
        self.available = False
        print(f"{self.title}: {self.available}")


little_prince = Book("Little Prince", "Antoine de Saint-Exupery", "novel", True)
print(little_prince.available)
little_prince.borrow()
print(little_prince.available)
