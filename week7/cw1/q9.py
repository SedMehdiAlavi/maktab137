#
# class Cart:
#     def __init__(self, items: list):
#         self.items = items
#
#
#     def __len__(self):
#         return len(self.items)
#
#     def __add__(self, other):
#         return Cart(self.items + other.items)
#
#     def __str__(self):
#         return f"Cart: {self.items}"
#
#     def __del__(self):
#         print('Cart cleared!')
#
#
# cart1 = Cart([('Laptop', 100), ('PS', 50)])
# cart2 = Cart([('Laptop', 100), ('PS', 50)])
# print(cart1 + cart2)
#
#

class ContactBook:
    contacts = {}
    def __init__(self, name , number):
        self.name = name
        self.numbers = number
        ContactBook.contacts[name] = number


    def __len__(self):
        return len(ContactBook.contacts)

    def __add__(self, other):
        return ContactBook(self.name + other.name, self.numbers + other.numbers)

    def __str__(self):
        return f"Name: {self.name}, Numbers: {self.numbers}"

    def __del__(self):
        print('Object deleted!')

contact1 = ContactBook('parsa', 123456)
contact2 = ContactBook('mehdi', 654321)
print(ContactBook.contacts)
print(contact1 + contact2)