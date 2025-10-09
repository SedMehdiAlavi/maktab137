
Prices = {"Apple": 60, "Banana": 20, "Orange": 45, "Grapes": 80}
print(Prices.keys())
products = {}

for key, value in Prices.items():
    if value > 50:

        products[key] = value - value / 10

print(products)