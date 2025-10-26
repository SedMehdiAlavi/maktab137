class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} {self.price}"

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.brand == other.brand and self.model == other.model and self.price == other.price

    def __add__(self, other):
        if isinstance(other, Car):
            return Car(self.brand, self.model, self.price + other.price)

    def __del__(self):
        print(self.brand, 'deleted')

car1 = Car('Saypa', 'Pride', 100)
car2 = Car('IKCO', 'Pars', 200)
print(car1 == car2)