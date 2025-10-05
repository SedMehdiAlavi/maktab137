def numbers():
    try:
        num = input("Enter a number: ")
        return int(num)
    except ValueError:
        return "Enter a number, not a string"

print(numbers())