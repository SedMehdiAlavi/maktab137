from functools import reduce

products = [
    {"name" : "laptop" , "price" : 1500, "quantity" : 2},
    {"name" : "mouse" , "price" : 25, "quantity" : 10},
    {"name" : "keyboard" , "price" : 75, "quantity" : 5}
]
# total = reduce(lambda total_price, product: total_price + product["price"] * product["quantity"], products, 0)
# print(total)

total = reduce(lambda total, product: total + product["price"] * product["quantity"], products, 0)
print(total)