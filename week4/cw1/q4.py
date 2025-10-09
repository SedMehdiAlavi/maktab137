def fib_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

generator = fib_generator(5)
print(generator)
for i in generator:
    print(i)