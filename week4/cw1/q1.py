numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(map(lambda number: number** 3, filter(lambda x: x % 2 != 0, numbers)))
result1 = [x**3 for x in numbers if x % 2!= 0]
print(result)
print(result1)