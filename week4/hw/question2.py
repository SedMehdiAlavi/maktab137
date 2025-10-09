def stringer(func):
    """
    This decorator print and return string-converted the
      main argument.
    """
    def wrapper(a):
        result = func(a)
        output = str(result)
        print(output)
        return output
    return wrapper

def lengther(func):
    """
    This decorator return length-calculated the main argument that
      converted to string in the previous decorator.
    """
    def wrapper(b):
        result = func(b)
        output = len(result)
        return output
    return wrapper

# """
# When two or more decorators use for function, below decorator
#   takes precedence over other decorator(s) tu run, so it runs and
#   returns to other decorators.
# """

@lengther
@stringer
def take_input(input):
    """
    It's a simple function that takes input as an argument and
      returns it.
    """
    return input


print(take_input(123456789))