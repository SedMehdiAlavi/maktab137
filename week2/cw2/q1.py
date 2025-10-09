def divide():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    try:
        return num1 / num2

    except ZeroDivisionError:
        return "Enter a valid number"


print(divide())