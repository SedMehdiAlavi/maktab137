# # id, title, author, publish date, gener, available
#
# BOOKS = (
#     (1, "داستان", 1943, "آنتوان دو سنت اگزوپری", "شازده کوچولو", True),
#     (2, "تخیلی-علمی", 1949, "جورج اورول", "1984", True),
#     (3, "اقتصاد", 1776, "آدام اسمیت", "ثروت ملل", False),
#     (4, "تاریخ", 2011, "یووال نوح هراری", "انسان خردمند", True),
#     (5, "داستان", 1988, "پائولو کوئلیو", "کیمیاگر", True),
#     (6, "داستان", 1967, "گابریل گارسیا مارکز", "صد سال تنهایی", False),
#     (7, "فانتزی", 1997, "جی. کی. رولینگ", "هری پاتر و سنگ جادو", True),
#     (8, "تاریخ", 1925, "آدولف هیتلر", "نبرد من", True),
#     (9, "اقتصاد", 1997, "رابرت کیوساکی", "پدر پولدار پدر بی‌پول", True),
#     (10, "شعر", 1390, "حافظ شیرازی", "دیوان حافظ", True)
# )
#
# #part1
# def convert_to_list(book_tuple):
#     books = []
#     for book in book_tuple:
#         books.append({
#             "id": book[0],
#             "genre": book[1],
#             "publish_date": book[2],
#             "author": book[3],
#             "title": book[4],
#             "available": book[5]
#         })
#     return books
# books_list = convert_to_list(BOOKS)
# print(books_list)
#
# #part2
# def sort_books(dictionary):
#     return dictionary["publish_date"], dictionary["id"]
#
# sorted_books = sorted(books_list, key=sort_books, reverse=True)
# print(sorted_books)
#
# #part3
# def available(book_tuple):
#     available_book = []
#     try:
#
#         for book1 in book_tuple:
#             if book1[5]:
#                 available_book.append({
#                 "title" : book1[4]
#                 })
#
#         return available_book
#
#     except IndexError:
#         print("error")
#
#
# print(available(BOOKS))
# available(BOOKS)
#
# #part4
# def rented_book(book_tuple):
#     rented_book = []
#
#     for book in book_tuple:
#         question = input(f"Is {book[4]} rented? ")
#         if question == "yes":
#             rented_book.append({
#                 "title" : book[4]
#             })
#
#     return rented_book
#
#
# rent = rented_book(BOOKS)
# print(rent)
#
# #part5
#
import itertools
counter = itertools.count(start=1, step=2)
print("Generating numbers(Itertools.count)".center(50, '-'))
for index in range(10):
    print(next(counter))