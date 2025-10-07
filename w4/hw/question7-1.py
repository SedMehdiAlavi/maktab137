def add(a, b, /):
    """
    It adds two numbers and returns sum of them. The arguments are
    positional only, so you can't define the by a keyword when
    calling. It puts the first value into the first argument and
    the second one into the second argument.
    """
    return a + b

print(add(2, 3))