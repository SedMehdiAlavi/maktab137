products = [
    {'name': 'A', 'price': 150, 'rating': 4.5},
    {'name': 'B', 'price': 200, 'rating': 4.2},
    {'name': 'C', 'price': 120, 'rating': 4.5},
    {'name': 'D', 'price': 250, 'rating': 4.8},
    {'name': 'E', 'price': 180, 'rating': 4.2}
]

sorted_products = sorted(products, key= lambda x: (-x['rating'], x['price']))

for product in sorted_products:
    print(product)
