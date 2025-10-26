class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        if isinstance(other, Product) and self.name == other.name:
            return Product(self.name, self.price, self.quantity + other.quantity)

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.quantity == other.quantity

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def __del__(self):
        print('Product deleted!')

# product1 = Product('Laptop', 100, 10)
# product2 = Product('Laptop', 200, 15)
# print(product1 + product2)