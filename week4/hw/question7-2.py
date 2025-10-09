def identity(*, name, age):
    """
    It prints a sentence with name and age. The arguments are
     keyword only, so you should use them by keyword when calling
     and you can change their position.
    """
    print(f"I am {name}, and I am {age} years old.")

identity(name='John', age=20)