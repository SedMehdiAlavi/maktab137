from abc import ABC, abstractmethod
import pickle
import os
from datetime import datetime, timedelta

data_file = 'library_data.pkl'
class Member(ABC):
    member_id = 1234
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.member_id = Member.member_id
        Member.member_id += 1
        self.borrowed_books = []


    @abstractmethod
    def borrow_book(self, book):
        if not book.is_borrowed:
            date = datetime.now()
            till = date + timedelta(days=14)

            self.borrowed_books.append(book)
            book.mark_as_borrowed(self.member_id)

        else:
            raise Exception('Book already borrowed')

    @abstractmethod
    def return_book(self, book):
        if book.is_borrowed:
            self.borrowed_books.remove(book)
            book.mark_as_returned(self)

        else:
            raise Exception('Book is not borrowed')

    @abstractmethod
    def show_info(self):
        print(f'{self.member_id}: {self.name} | {self.email}')
        for book in self.borrowed_books:
            print(book.display_info())



class StudentMember(Member):
    def __init__(self, name, email):
        super().__init__(name, email)

    def borrow_book(self, book):
        if len(self.borrowed_books) < 3:
            super().borrow_book(book)
        else:
            raise Exception('You cannot borrow more than 3 books')

    def return_book(self, book):
        super().return_book(book)

    def show_info(self):
        super().show_info()



class TeacherMember(Member):
    def __init__(self, name, email):
        super().__init__(name, email)

    def borrow_book(self, book):
        if len(self.borrowed_books) < 5:
            super().borrow_book(book)
        else:
            raise Exception('You cannot borrow more than 5 books')

    def return_book(self, book):
        super().return_book(book)

    def show_info(self):
        super().show_info()




class Book:
    total_books = 0
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        Book.total_books += 1
        self.is_borrowed = False
        self.current_borrower_id = None
        self.borrow_date = None
        self.due_date = None

    def mark_as_borrowed(self, borrower_id):
        self.is_borrowed = True
        self.current_borrower_id = borrower_id
        self.borrow_date = datetime.now().date()
        self.due_date = self.borrow_date + timedelta(days=5)

    def mark_as_returned(self):
        self.is_borrowed = False
        self.current_borrower_id = None

    def display_info(self):
        available = f'Borrower: {self.current_borrower_id} | {self.borrow_date} - {self.due_date}' if self.current_borrower_id else 'Available'
        return f'{self.title} | {self.author} | {self.isbn} | {available}'


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.members = []


    def save(self):
        with open(data_file, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load():
        if os.path.exists(data_file):
            with open(data_file, 'rb') as file:
                return pickle.load(file)
        return Library('My Library')

    def add_book(self, *book: Book):
        for book in book:
            self.books.append(book)
        self.save()

    def add_member(self, member: Member):
        for m in self.members:
            if m.email == member.email:
                raise Exception('Member already added')
        self.members.append(member)
        self.save()

    def find_member_by_id(self, member_id: int):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_book_by_isbn(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def borrow_book(self, member_id: int, isbn):
        member = self.find_member_by_id(member_id)
        if not member:
            raise Exception('Member not found')

        book = self.find_book_by_isbn(isbn)
        if not book:
            raise Exception('Book not found')

        if book.is_borrowed:
            raise Exception('Book is already borrowed')
        try:
            for m in self.members:
                if m.member_id == member_id:
                    m.borrow_book(book)
                    book.mark_as_borrowed(member_id)
        except ValueError:
            raise 'Book already borrowed'
        self.save()

    def return_book(self, member_id: int, isbn):
        member = self.find_member_by_id(member_id)
        if not member:
            raise Exception('Member not found')

        book = self.find_book_by_isbn(isbn)
        if not book:
            raise Exception('Book not found')

        if not book.is_borrowed:
            raise Exception('Book is not borrowed')
        try:
            for m in self.members:
                if m.member_id == member_id:
                    m.return_book(book)
                    book.mark_as_returned()
        except ValueError:
            raise 'Book already borrowed'
        self.save()

    def search_book_by_title(self, title: str):
        for book in self.books:
            if book.title == title:
                return book.display_info()

    def search_member_by_name(self, name: str):
        for member in self.members:
            if member.name == name:
                print(f"{member.member_id}: {member.name} | {member.email}")
        for book in member.borrowed_books:
            print(book.display_info())



    def show_all_books(self):
        print(f'Welcome to {self.name} library'.center(50, '-'))
        for book in self.books:
            print(book.display_info())

    def show_all_members(self):
        for member in self.members:
            print(f'{member.member_id}: {member.name} | {member.email} :')
            for book in member.borrowed_books:
                print(book.display_info())

    def books_status(self):
        print('Available books'.center(50, '-'))
        for book in self.books:
            if not book.is_borrowed:
                print(book.display_info())

        print('\n','Borrowed books'.center(50, '-'))
        for book in self.books:
            if book.is_borrowed:
                print(book.display_info())

if os.path.exists('library_data.pkl'):
    lib1 = Library.load()
else:
    lib1 = Library('My Library')

print(lib1.members)



book1 = Book('Little Prince', 'Antoine Exupery', '123456')
book2 = Book('The Great Gatsby', 'Scott Fitzgerald', '789123')
book3 = Book('Jane Eyre', 'Charlotte Bronte', '456789')
book4 = Book('Anna Karenina', 'Leo Tolstoy', '123789')
book5 = Book('War and Peace', 'Leo Tolstoy', '159753')
book6 = Book('David Copperfield', 'Charles Dickens', '357951')
book7 = Book('Crime and Punishment', 'Fyodor Dostoevsky', '236248')
book8 = Book('Robinson Crusoe', 'Daniel Defoe', '224339')
book9 = Book('The Midnight Library', ' Matt Haig', '246810')
book10 = Book('A Fraction of the Whole', ' Steve Toltz', '135790')

member1 = StudentMember('Sed Mehdi', 'mehdi@example.com')
member2 = TeacherMember('Parsa', 'parsa@example.com')

hafez = Library('Hafez')
hafez.add_member(member1)
hafez.add_member(member2)

hafez.add_book(book1, book2, book3, book4, book5, book6, book7, book8, book9, book10)

member1.borrow_book(book1)
member1.borrow_book(book2)
member2.borrow_book(book3)
member2.borrow_book(book4)

# hafez.borrow_book(1234, '123456')
# hafez.borrow_book(1234, '123456')
# hafez.show_all_members()
# hafez.search_member_by_name('Sed Mehdi')
# hafez.books_status()
print(hafez.load())
print(lib1.show_all_members())

