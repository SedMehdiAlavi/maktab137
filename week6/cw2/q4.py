class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell(self, quantity: int):
        self.quantity -= quantity

    def restock(self, quantity: int):
        self.quantity += quantity

    def display_info(self):
        print(f"Name: {self.name} \nPrice: {self.price} $ \nQuantity: {self.quantity}")

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def update_product(self, product: Product, price: float):
        product.price = price

    def delete_product(self, product: Product):
        self.products.remove(product)

    def read_inventory(self):
        for product in self.products:
            print(f"{product.name} : {product.price} $ | Quantity: {product.quantity}")


lipstick = Product("Lipstick", 5.0, 10)
deodorant = Product("Deodorant", 4.0, 20)


mahdie = Inventory()
mahdie.add_product(lipstick)
mahdie.add_product(deodorant)

