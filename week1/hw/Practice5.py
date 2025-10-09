#for
number: int = 6
factor = 1

for i in range(1, number + 1):

    factor *= i

print(factor)


#while
number: int = 6
factor = 1

while number > 1:

    factor *= number
    number -= 1

print(factor)
