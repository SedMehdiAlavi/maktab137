
def check_input(x):
    """
    In Python, the isinstance() function checks whether
    an object is an instance of a specified type,
    class, or a tuple of classes. If it is, the function returns True,
    otherwise it returns False .
    This check is useful for type validation in functions, debugging,
    and ensuring safe operations on data structures.
    """
    if isinstance(x, int):
        return x*x
    elif isinstance(x, str):
        return len(x)
    elif isinstance(x, list):
        return sum(x)
    else:
        return "Wrong!"
# isinstance
print(check_input(5))
print(check_input("salam"))
print(check_input([1,2,3]))