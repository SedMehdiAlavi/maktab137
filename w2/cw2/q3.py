def myfun():
    while True:
        x = input("Enter a number: ")
        try:
            num = float(x)
            if num < 0 :
                raise ValueError("Enter a positive number\n")
            print(x,'\n')

        except ValueError as error:
            print(f"Error: {error}\n")


myfun()
