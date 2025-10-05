while True:
    x = int(input("Enter a number: "))
    select = int(input("Enter an operation: "))

    def operation(x, select):

        def double(n):
            return n * 2

        def triple(n):
            return n * 3

        if select == 2:
            return double(x)
        elif select == 3:
            return triple(x)
        else:
            raise ValueError("Wrong operation")

    print(operation(x, select))