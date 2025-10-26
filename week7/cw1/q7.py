class Library:
    def __init__(self,books: list):
        self.books = books


    def __len__(self):
        return len(self.books)

    def __add__(self, other):
        if isinstance(other, Library):
            return Library(self.books + other.books)

    def __str__(self):
        c = 1
        for book in self.books:
            print(f'{c}: {book}')
            c += 1
        return f'{self.books}'

    def __del__(self):
        print('Deleted')



l1 = Library(['a', 'b', 'c', 'd'])
l2 = Library(['e', 'f', 'g', 'h'])
print(l1 + l2)
print(len(l1))
